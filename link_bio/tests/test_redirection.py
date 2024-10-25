from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = '/usr/bin/chromedriver'

def test_redireccion_github():
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get('http://localhost:3000')
    
    boton_github = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://github.com/raulblend"]'))
    )
    boton_github.click()

    time.sleep(2)

    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

    WebDriverWait(driver, 10).until(EC.url_contains('https://github.com/raulblend'))



    assert driver.current_url == 'https://github.com/raulblend', f"URL actual es {driver.current_url}"

    driver.quit()
    
#test_redireccion_linkedin()
test_redireccion_github()