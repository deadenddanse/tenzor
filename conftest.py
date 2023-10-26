import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/home/antonmorozov/tenzor/data"}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    yield driver
    driver.quit()
