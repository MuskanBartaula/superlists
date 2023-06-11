from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'H:/Tutorial/Testing/lib/chromedriver.exe'
service = Service(executable_path=DRIVER_PATH)
chrome_options = Options()
chrome_options.binary_location='C:/Program Files/Google/Chrome/Application/chrome.exe'
chrome_options.add_argument('--no-sandbox')

browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('http://localhost:8000')

assert 'The' in browser.title, "The is not in title"