from selenium import webdriver
from locators import Locators

class Registration:

    # Регистрация нового пользователя
    def test_01_new_user_registration(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_personal_account_button().click()

        locators.get_registration_link().click()

        locators.get_input_field_name().send_keys("Федор")

        locators.get_input_field_email().send_keys("Fedor@ya.ru")

        locators.get_input_field_password().send_keys("parol123")

        locators.get_registration_button().click()

        driver.quit()

    # Ошибка на некорректный пароль
    def test_02_incorrect_password(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_personal_account_button().click()

        locators.get_registration_link().click()

        locators.get_input_field_name().send_keys("Петор")

        locators.get_input_field_email().send_keys("Petor@ya.ru")

        locators.get_input_field_password().send_keys("parol")

        locators.get_registration_button().click()

        # Что добавить для проверки некорректного пароля?

        driver.quit()

registration = Registration()
registration.test_01_new_user_registration()
registration.test_02_incorrect_password()