from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import existing_user_data


class TestLogin:
    def test_user_login(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(LOGIN_LABEL))

        driver.find_element(*EMAIL_INPUT).send_keys(existing_user_data['exist_email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(existing_user_data['exist_password'])
        driver.find_element(*LOGIN_PAGE_BUTTON).click()

        avatar_logo = wait.until(EC.visibility_of_element_located(USERS_LOGO))
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME))

        assert avatar_logo.is_displayed(), 'Аватар пользователя не отображается'
        assert user_name.is_displayed(), 'Имя пользователя не отображается'
        assert "User" in user_name.text, 'Имя пользователя не содержит "User"'
