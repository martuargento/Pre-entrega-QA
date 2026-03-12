from page.login_page import Login_Page
from page.inventario_page import inventario_page
import time


def test_inventario(driver):
    login = Login_Page(driver)
    inventario = inventario_page(driver)

    login.navegar_a_url_login()
    login.login()

    time.sleep(10)

    inventario.en_pagina_de_inventario()

    inventario.logout()
    time.sleep(5)
    assert "https://www.saucedemo.com/" in driver.current_url 