from bs4 import BeautifulSoup
from xmltodict import parse as parseXml

from webdriver_installer.core.driver_installer import DriverInstaller


class Chrome(DriverInstaller):
    def __init__(self):
        super().__init__(name='chromedriver',
                         filename='chromedriver',
                         base_url='https://chromedriver.storage.googleapis.com',
                         version_url='https://chromedriver.storage.googleapis.com/LATEST_RELEASE')

    def get_download_url(self, version: str, bit: str) -> str:
        if bit == '64':
            print('As of this version chromedriver-64 bit does not exist, '
                  'chromedriver-32bit will be downloaded instead')
        TARGET = f'win32.zip'
        URL = f'https://chromedriver.storage.googleapis.com/?delimiter=/&prefix={version}/'
        response = self.request(URL)
        if not response:
            raise Exception(f'Failed to fetch download link for {self.name} {bit}-bit')
        results = parseXml(response.text)['ListBucketResult']['Contents']
        for element in results:
            if TARGET in element['Key']:
                download_url = self.base_url + '/' + element['Key']
                return download_url
        raise Exception(f'Could not find download url for {self.name} {bit}-bit')
