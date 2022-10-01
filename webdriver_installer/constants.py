from os import getlogin

user_name = getlogin()

# FireFox
GECKO_DOWNLOAD_URL = "https://github.com/mozilla/geckodriver/releases"
GECKO_VERSION_URL = "https://github.com/mozilla/geckodriver/releases/latest"
GECKO_INSTALL_DIR = f"C:/Users/{user_name}/AppData/Roaming/webdrivers/geckodriver"

# Google Chrome
CHROME_VERSION_URL = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
CHROME_DOWNLOAD_URL = "https://chromedriver.storage.googleapis.com"
CHROME_INSTALL_DIR = f"C:/Users/{user_name}/AppData/Roaming/webdrivers/chromedriver"

# Opera
OPERA_VERSION_URL = "https://github.com/operasoftware/operachromiumdriver/releases/latest"
OPERA_DOWNLOAD_URL = "https://github.com/operasoftware/operachromiumdriver/releases/download"
OPERA_INSTALL_DIR = f"C:/Users/{user_name}/AppData/Roaming/webdrivers/operadriver"

# Microsoft Edge
EDGE_VERSION_URL = "https://msedgedriver.azureedge.net/LATEST_STABLE"
EDGE_DOWNLOAD_URL = "https://msedgedriver.azureedge.net"
EDGE_INSTALL_DIR = f"C:/Users/{user_name}/AppData/Roaming/webdrivers/edgedriver"