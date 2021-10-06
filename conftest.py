import pytest
from selenium import webdriver

from Config.TestData import TestData


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    yield driver
    driver.quit()
