import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        # Mukesh heard a cool todo list site on the internet. He visit the site via chrome.
        self.browser.get('http://localhost:8000')
        
        # He looks the title of the site and 
        # notice the title and header is "TO-DO!"
        title = 'TO-DO'
        self.assertIn(title, self.browser.title)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
  
        self.assertIn(header.text, title)


if __name__ == '__main__':
    unittest.main()
