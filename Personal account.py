from selenium import webdriver
from locators import Locators

class PersonalAccount:

    # Переход в личный кабинет
    def test_01_go_to_personal_account(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_personal_account_button().click()

        driver.quit()

    # Переход из личного кабинета в Конструктор
    def test_02_jump_to_constructor(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_personal_account_button().click()

        locators.get_button_constructor().click()

        driver.quit()

    # Переход из личного кабинета по логотипу
    def test_03_transition_by_logo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_personal_account_button().click()

        locators.get_logo().click()

        driver.quit()

personal_account = PersonalAccount()
personal_account.test_01_go_to_personal_account()
personal_account.test_02_jump_to_constructor()
personal_account.test_03_transition_by_logo()
