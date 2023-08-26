from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
# options = Options().add_experimental_option("detach", True)


def test_one():
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.google.com/")
    assert driver
