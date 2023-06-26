from django.test import LiveServerTestCase
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


DRIVER_PATH = 'H:/Tutorial/Testing/lib/chromedriver.exe'
BINARY_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

MAX_WAIT = 10

class HomePageTest(LiveServerTestCase):
    
    def setUp(self) -> None:
        self.service = Service(executable_path=DRIVER_PATH)
        self.chrome_options = Options()
        self.chrome_options.binary_location= BINARY_PATH
        # self.chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # Mukesh heard a cool todo list site on the internet. He visit the site via chrome.
        self.browser.get(self.live_server_url)
        
        # He looks the title of the site and 
        # notice the title and header is "TO-DO"
        title = 'TO-DO'
        self.assertIn(title, self.browser.title)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
  
        self.assertIn(header.text, title)
        
        # He see a textbox where he can enter some todo items
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        
        # He enter some to-do items
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("2: Use peacock feathers to make fly")

        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make fly")

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith visit the site
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        
        self.browser.quit()
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)
        
        # Francis visit the site. There's no sign of Edith's content
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')

        self.assertNotEqual(edith_list_url, francis_list_url)
        
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNoIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        

