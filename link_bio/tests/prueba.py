from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Especifica la ruta a tu chromedriver
chromedriver_path = '/usr/bin/chromedriver'

# Usar la clase Service para iniciar ChromeDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Ahora puedes realizar las operaciones en tu aplicación
driver.get('https://www.google.com')  # Cambia por la URL de tu app
print(driver.title)
driver.quit()
