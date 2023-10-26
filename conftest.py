import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    chromeOptions = webdriver.ChromeOptions()
    download_folder = "/home/antonmorozov/tenzor/data"
    prefs = {"download.default_directory": download_folder}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    yield driver
    driver.quit()
