from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *
from data import test_usual_password, ad_title
from helpers import unique_email

class TestCreateAds:

    def test_create_ad_authorized_user(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(REGISTRATION_LABEL))

        email = unique_email()
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CREATE_ACC_BUTTON).click()

        wait.until(EC.visibility_of_element_located(USERS_LOGO))
        wait.until(EC.visibility_of_element_located(USER_NAME))

        driver.find_element(*CREATE_AD_BUTTON).click()
        driver.find_element(*TITLE_INPUT).send_keys(ad_title['ads_title'])
        driver.find_element(*CONDITION_RADIOBUTTON_USED).click()
        driver.find_element(*DESCRIPTION_TEXTAREA).send_keys(ad_title['description_ads'])
        driver.find_element(*PRICE_INPUT).send_keys(str(ad_title['price_ads']))

    def test_create_ad_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.find_element(*CREATE_AD_BUTTON).click()
        auth_error = wait.until(EC.visibility_of_element_located(AUTH_ERROR))
        assert 'Чтобы разместить объявление, авторизуйтесь' in auth_error.text, f'текст не соответствует {auth_error.text}'