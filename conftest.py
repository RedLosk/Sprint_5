import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.get("https://qa-desk.stand.praktikum-services.ru/")

    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def unique_email():
    import time
    return f"test_user_{int(time.time())}@example.com"