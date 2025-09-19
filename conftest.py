import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture
def driver():
    url = Urls().test_url
    driver = webdriver.Chrome()
    driver.get('https://qa-desk.stand.praktikum-services.ru')
    driver.get(url)

    yield driver
    driver.quit()