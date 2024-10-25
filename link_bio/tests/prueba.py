from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chromedriver_path = '/usr/bin/chromedriver'


service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://www.google.com')
driver.quit()
