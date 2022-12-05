import os
import sys
from zipfile import ZipFile

import requests
from packaging.version import parse as parse_version
from webdriver_installer.utils import user_agent, print_error, print_warning, print_green

# --- Setup the install path ---
USERNAME = os.getlogin()
USER_PATH = f'C:/Users/{USERNAME}/AppData/Roaming/webdrivers/'
if not os.path.exists(USER_PATH):
    os.makedirs(USER_PATH)


class DriverInstaller:
    SAVE_PATH = USER_PATH

    def __init__(self, name='Installer', filename='driver', base_url='', version_url=''):
        self.name = name
        self.filename = filename
        self.base_url = base_url
        self.version_url = version_url
        self.driver_dir = os.path.join(self.SAVE_PATH, self.name + '_folder/')
        if not os.path.exists(self.driver_dir):
            os.makedirs(self.driver_dir)
        self.version_dir = os.path.join(self.driver_dir, 'version')
        self.curr_driver = None

    @property
    def path(self) -> str:
        if self.curr_driver is None:
            self.install()
        return os.path.join(self.driver_dir, self.curr_driver)

    def install(self, bit: int = 32) -> str:
        if bit not in (32, 64):
            print_warning(f'{bit}-bit does not exist, it was set to 32-bit instead')
            bit = str(bit)
        else:
            bit = str(bit)
        # -- Vars --
        filename = self.filename + bit + '.exe'
        self.curr_driver = filename
        # -- Check current version --
        curr_version = self.current_version(bit)
        latest_version = self.latest_version()
        if self.is_latest_version(current=curr_version, latest=latest_version):
            print(f'You already have the latest version of {self.name}-{bit}bit installed ({latest_version})')
            return self.path
        print(f'Driver {self.name}-{bit}bit version {latest_version} found...')
        # -- Download the driver zip file --
        download_url = self.get_download_url(version=latest_version, bit=bit)
        zip_file_path = self.download(url=download_url, version=latest_version)
        # -- Extract the driver and delete the zip file --
        self.exe_from_zip(zip_file_path, self.driver_dir + filename)
        os.remove(zip_file_path)
        print_green(f'{self.name.capitalize()}-{bit}bit version {latest_version} was installed successfully')
        # -- Save the latest version --
        self.save_version(version=latest_version, bit=bit)
        # -- Return the driver exe file path --
        return self.path

    def current_version(self, bit: str) -> str:
        version_file = self.version_dir + bit
        if not os.path.exists(version_file):
            return ''

        with open(version_file, 'r') as f:
            data = f.readlines()
            return data[0]

    def latest_version(self) -> str:
        response = self.request(self.version_url)
        if not response:
            raise Exception(f'Could not get latest version number for {self.name}')
        version_from_url = response.url.split('/')[-1]
        is_version = any(char.isdigit() for char in version_from_url)
        if is_version:
            return version_from_url

        return response.text.strip()

    def download(self, url: str, version: str) -> str:
        try:
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                raise Exception(f"Failed to start {self.name} download")
        except:
            raise Exception("Could not connect to download server")

        # Download and save file as zip
        zip_file_path = self.driver_dir + self.name + '.zip'
        try:
            with open(zip_file_path, "wb") as f:
                print(f'Downloading {self.name} version {version}...')
                progress = 0
                total_length = int(response.headers.get('content-length'))
                for data in response.iter_content(chunk_size=4096):
                    progress += len(data)
                    f.write(data)
                    done = int(50 * progress / total_length)
                    finished_percentage = '=' * done
                    left_percentage = ' ' * (50 - done)
                    progress_percentage = (progress / total_length) * 100
                    sys.stdout.write(f"\r[{finished_percentage}{left_percentage}] {progress_percentage:.2f}%")
                    sys.stdout.flush()
                print('')
        except:
            raise Exception('Lost connection to server while downloading file')

        return zip_file_path

    def get_download_url(self, version: str, bit: str) -> str:
        """
        Creates the download link for the driver file
        Must be implemented for each installer individually
        :return: str (the download link)
        """
        pass

    def is_latest_version(self, current: str, latest: str) -> bool:
        if parse_version(current) < parse_version(latest):
            return False
        if not os.path.exists(self.path):
            return False

        return True

    def save_version(self, version: str, bit: str) -> None:
        version_file = self.version_dir + bit
        with open(version_file, "w") as f:
            f.write(version)

    @staticmethod
    def exe_from_zip(zip_path, file_path) -> None:
        if not os.path.exists(zip_path):
            raise Exception(f"{zip_path} does not exist")
        with ZipFile(zip_path, "r") as zf:
            exe_path = None
            for name in zf.namelist():
                if name.endswith(".exe"):
                    exe_path = name
                    break
            if exe_path is None:
                raise Exception("Driver executable not found in zip file.")
            with open(file_path, "wb") as f:
                f.write(zf.read(exe_path))

    @staticmethod
    def request(url, headers=None) -> requests.Response | None:
        headers = {'user-agent': user_agent()} if headers is None else headers
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response
        except:
            print_error(f'Failed to connect to {url}')
