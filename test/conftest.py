import pytest
from utils.helpers import get_driver

@pytest.fixture
def driver():
     #configuracion para consultar a selenium web drive
     driver = get_driver()
     yield driver
     driver.quit()