import os
import sys

import requests
from requests import Response

from webdriver_installer.constants import CHROME_VERSION_URL, CHROME_DOWNLOAD_URL, CHROME_INSTALL_DIR
from webdriver_installer.default_driver import DefaultDriver


class ChromeDriver(DefaultDriver):
    def __init__(self):
        super().__init__(name="ChromeDriver",
                         file_name="chromedriver",
                         bit=32,
                         version_url=CHROME_VERSION_URL,
                         download_url=CHROME_DOWNLOAD_URL,
                         install_path=CHROME_INSTALL_DIR)

    def __str__(self):
        return self.driver_path

    def __repr__(self):
        return self.driver_path

    def _getLatestVersion(self) -> str:
        try:
            response = requests.get(self._version_url)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch latest version number for {self._driver_name}")
            return response.text
        except:
            print("Connection to server failed. Check your internet and try again")
            return ""

    def _downloadDriver(self, version) -> bool:
        URL = f"{self._download_url}/{version}/chromedriver_win{self._bit}.zip"
        # Initiate response variable to use in a try catch
        response: Response
        try:
            response = requests.get(URL, stream=True)
            if response.status_code != 200:
                raise Exception(f"Failed to start {self.driver_path} download")
        except:
            print("Could not connect to download server")
            return False

        # Download and save file as zip
        try:
            with open(self._zip_file, "wb") as f:
                print(f"Downloading {self._driver_name} version {version}...")
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
                print("")
        except:
            print("Lost connection to server while downloading file")
            return False

        # Extract file to same dir
        try:
            self.exe_from_zip(self._zip_file, self._driver_path)
        except Exception as e:
            print(e)
            print("Failed to extract the driver zip file")
            return False

        # Save version number to file
        self._saveVersion(version)

        # Delete zip file
        os.remove(self._zip_file)
        return True
