from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import existing_user_data, test_usual_password

class TestRegistration:

    def test_new_user_registration_valid_email_format(self, driver, wait, unique_email):
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))

        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
        driver.find_element(*EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CREATE_ACC_BUTTON).click()

        avatar_logo = wait.until(EC.visibility_of_element_located(USERS_LOGO))
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))

        assert avatar_logo.is_displayed(), 'Аватар пользователя не отображается'
        assert user_name.is_displayed(), 'Имя пользователя не отображается'
        assert "User" in user_name.text, 'Имя пользователя не содержит "User"'

    def test_new_user_registration_unsupported_email_format(self, driver, wait):
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))

        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
        driver.find_element(*EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(*PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CREATE_ACC_BUTTON).click()

        email_error = wait.until(EC.visibility_of_element_located(EMAIL_ERROR))
        assert email_error.is_displayed(), 'Ошибка не появилась'
        assert email_error.text == "Ошибка", 'Текст ошибки не соответствует'

    def test_registration_already_registered_user(self, driver, wait):

        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))

        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT))
        driver.find_element(*EMAIL_INPUT).send_keys(existing_user_data['exist_email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(existing_user_data['exist_password'])
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(existing_user_data['exist_password'])
        driver.find_element(*CREATE_ACC_BUTTON).click()

        email_error = wait.until(EC.visibility_of_element_located(EMAIL_ERROR))
        assert email_error.is_displayed(), 'Ошибка не появилась'
        assert email_error.text == "Ошибка", 'Текст ошибки не соответствует'