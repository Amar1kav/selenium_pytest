import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv = Service(ChromeDriverManager().install())
opt = Options().add_experimental_option("detach", True)

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=serv, options=opt)
    driver.get("https://www.youtube.com/")
    driver.implicitly_wait(10)
    return driver
