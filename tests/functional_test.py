import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = 'H:/Tutorial/Testing/lib/chromedriver.exe'
BINARY_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

class HomePageTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.service = Service(executable_path=DRIVER_PATH)
        self.chrome_options = Options()
        self.chrome_options.binary_location= BINARY_PATH
        self.chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def test_home_page(self) -> None:
        self.browser.get('http://localhost:8000')
        assert 'The install worked successfully!' in self.browser.title, "The is not in title"
    

if __name__ == '__main__':
    unittest.main()
