from bs4 import BeautifulSoup
from webdriver_installer.core.driver_installer import DriverInstaller


class FireFox(DriverInstaller):
    def __init__(self):
        super().__init__(name='geckodriver',
                         filename='geckodriver',
                         base_url='https://github.com',
                         version_url='https://github.com/mozilla/geckodriver/releases/latest')

    def get_download_url(self, version: str, bit: str) -> str:
        TARGET = f'win{bit}.zip'
        URL = f'https://github.com/mozilla/geckodriver/releases/expanded_assets/{version}'
        response = self.request(URL)
        if not response:
            raise Exception(f'Failed to fetch download link for {self.name} {bit}-bit')
        soup = BeautifulSoup(response.content, 'html.parser')
        links_elements = soup.find_all('a', href=True)
        for element in links_elements:
            if TARGET in element.text:
                download_url = self.base_url + element.get('href')
                return download_url
        raise Exception(f'Could not find download url for {self.name} {bit}-bit')
