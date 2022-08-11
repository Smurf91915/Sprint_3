from selenium import webdriver
from locators import Locators

class Login:

    # Вход по кнопке "Войти в аккаунт" на главной
    def test_01_log_in_to_the_main_account(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        driver.quit()

    # Вход через кнопку "Личный кабинет"
    def test_02_login_through_personal_account(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_personal_account_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        driver.quit()

    # Вход через кнопку в форме регистрации
    def test_03_login_via_registration_form(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_personal_account_button().click()

        locators.get_registration_link().click()

        locators.get_login_link().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        driver.quit()

    # Вход через кнопку в форме восстановления пароля
    def test_04_login_via_password_recovery_form(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_personal_account_button().click()

        locators.get_restore_password_link().click()

        locators.get_login_link().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        driver.quit()

login = Login()
login.test_01_log_in_to_the_main_account()
login.test_02_login_through_personal_account()
login.test_03_login_via_registration_form()
login.test_04_login_via_password_recovery_form()