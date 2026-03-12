from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"

def get_driver():
    # 1. Configuramos las opciones para el robot de GitHub Actions
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 2. Creamos el driver usando esas opciones
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(5)

    return driver