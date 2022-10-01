import os
import shutil
from zipfile import ZipFile

from packaging.version import parse as parse_version


class DefaultDriver:
    # Show debug messages
    DEBUG = True

    def __init__(self, name, file_name, version_url, download_url, install_path, bit):
        self._driver_name = f"{name}-{bit}bit"
        self._driver_file = file_name
        if bit not in (32, 64):
            self._bit = 32
            print(f"{bit}-bit doesnt exit. 32-bit was selected instead.")
        self._bit = bit
        self._version_url = version_url
        self._download_url = download_url
        self._install_path = install_path
        self._zip_file = f"{self._install_path}/driver.zip"
        self._version_file = f"{self._install_path}/version"
        self._driver_path = f"{self._install_path}/{file_name}{self._bit}.exe"

    @property
    def driver_path(self) -> str:
        # Check if file exist in destination
        if os.path.exists(self._driver_path):
            return self._driver_path
        else:
            return f"{self._driver_name} not found"

    def install(self, update=False) -> str:
        driver_exist = self._checkDriver(update)
        if driver_exist:
            return self.driver_path

        # Create driver folder
        if not os.path.exists(self._install_path):
            os.makedirs(self._install_path)

        # Start downloading the latest version
        latest_version = self._getLatestVersion()
        result = self._downloadDriver(latest_version)

        if not result:
            print(f"Failed to install {self._driver_name}")
            return ""

        print(f"Successfully installed {self._driver_name}")
        self.print_debug(f"Path : {self.driver_path}")
        return self.driver_path

    def _checkDriver(self, update) -> bool:
        if not os.path.exists(self._install_path):
            return False
        if not os.path.exists(self._driver_path):
            return False
        if not os.path.exists(self._version_file):
            return False
        # Check driver version
        version = parse_version(self._getVersion())
        latest_version = parse_version(self._getLatestVersion())
        if latest_version > version:
            if update:
                self.print_debug(f"===| New {self._driver_name} version found |===")
                self.print_debug(f"Updating from {version} to {latest_version}")
                return False
            else:
                self.print_debug(f"New {self._driver_name} version {latest_version} was found, but update is disabled.")
                return True

        return True

    def _getVersion(self) -> str:
        with open(self._version_file, "r") as f:
            return f.read().strip()

    def _saveVersion(self, version) -> None:
        with open(self._version_file, "w") as f:
            f.write(version)

    def uninstall(self):
        shutil.rmtree(self._install_path)
        print(f"{self._driver_name} was successfully uninstalled.")

    @staticmethod
    def exe_from_zip(zip_path, file_path):
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
    def print_debug(msg):
        if DefaultDriver.DEBUG:
            print(msg)

    def _getLatestVersion(self) -> str:
        pass

    def _downloadDriver(self, version) -> bool:
        pass
