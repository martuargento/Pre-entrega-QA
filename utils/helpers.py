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

    # LAS 3 LÍNEAS MÁGICAS PARA GITHUB ACTIONS
    chrome_options.add_argument("--headless")               # Sin ventana
    chrome_options.add_argument("--no-sandbox")             # Bypass de seguridad de Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # Usa memoria compartida (evita crashes)
    
    # Opcional pero recomendado para evitar otros errores
    chrome_options.add_argument("--window-size=1920,1080")

    # 2. Creamos el driver usando esas opciones
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(5)

    return driver