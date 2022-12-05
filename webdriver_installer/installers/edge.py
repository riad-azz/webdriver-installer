from bs4 import BeautifulSoup
from webdriver_installer.core.driver_installer import DriverInstaller


class Edge(DriverInstaller):
    def __init__(self):
        super().__init__(name='edgedriver',
                         filename='edgedriver',
                         base_url='https://msedgedriver.azureedge.net',
                         version_url='https://msedgedriver.azureedge.net/LATEST_STABLE')

    def get_download_url(self, version: str, bit: str) -> str:
        TARGET = f'win{bit}.zip'
        VERSION_NUMBER = version.split('.')[0]
        SELECTOR = f'Microsoft Edge WebDriver for release number {VERSION_NUMBER}'
        URL = f'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'
        response = self.request(URL)
        if not response:
            raise Exception(f'Failed to fetch download link for {self.name} {bit}-bit')
        soup = BeautifulSoup(response.content, 'html.parser')
        links_container = soup.find('nav', {'aria-label': SELECTOR})
        links_elements = links_container.find_all('a', href=True)
        for element in links_elements:
            temp_link = element.get('href')
            if TARGET in temp_link:
                download_url = temp_link
                return download_url
        raise Exception(f'Could not find download url for {self.name} {bit}-bit')