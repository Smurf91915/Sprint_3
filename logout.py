from selenium import webdriver
from locators import Locators

class Logout:

    # Выход из аккаунта в личном кабинете
    def test_01_leaving_the_account(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_personal_account_button().click()

        locators.get_exit_button().click()

        driver.quit()

logout = Logout()
logout.test_01_leaving_the_account()