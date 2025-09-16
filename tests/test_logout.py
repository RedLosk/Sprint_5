
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import existing_user_data, test_usual_password

class TestLogOut:
    def test_user_logout_existing_user(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(existing_user_data['exist_email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(existing_user_data['exist_password'])
        driver.find_element(*LOGIN_PAGE_BUTTON).click()

        wait.until(EC.visibility_of_element_located(USERS_LOGO))
        wait.until(EC.visibility_of_element_located(USER_NAME))

        logout_btn = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_btn.click()

        login_btn = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))

        avatar_elements = driver.find_elements(*USERS_LOGO)
        user_name_elements = driver.find_elements(*USER_NAME)

        assert login_btn.is_displayed(), 'Кнопка входа не отображается'
        assert len(avatar_elements) == 0, 'Аватар пользователя отображается'
        assert len(user_name_elements) == 0, 'Имя пользователя отображается'

    def test_user_logout_new_user(self, driver, wait, unique_email):
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))

        wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(REGISTRATION_LABEL))

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(test_usual_password)
        driver.find_element(*CREATE_ACC_BUTTON).click()

        wait.until(EC.visibility_of_element_located(USERS_LOGO))
        wait.until(EC.visibility_of_element_located(USER_NAME))

        logout_btn = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_btn.click()

        login_btn = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))

        avatar_elements = driver.find_elements(*USERS_LOGO)
        user_name_elements = driver.find_elements(*USER_NAME)

        assert login_btn.is_displayed(), 'Кнопка входа не отображается'
        assert len(avatar_elements) == 0, 'Аватар пользователя отображается'
        assert len(user_name_elements) == 0, 'Имя пользователя отображается'