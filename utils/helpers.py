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

    # 2. Modo invisible (obligatorio para GitHub)
    chrome_options.add_argument("--headless=new") 
    
    # 3. Argumentos de estabilidad para Linux (evitan el error que te salió)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # 4. Creamos el driver usando esas opciones
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(5)

    return driver