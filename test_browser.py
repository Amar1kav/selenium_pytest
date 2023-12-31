import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv = Service(ChromeDriverManager().install())
opt = Options().add_experimental_option("detach", True)

@pytest.mark.smoke
def test_add(setup):
    driver = setup
    assert driver.title == "YouTube"