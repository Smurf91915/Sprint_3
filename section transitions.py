from selenium import webdriver
from locators import Locators

class SectionTransitions:

    # Переход в раздел Булки
    def test_01_chapter_buns(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_buns_button().click()

        driver.quit()

    # Переход в раздел Соусы
    def test_02_chapter_sauces(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_sauce_button().click()

        driver.quit()

    # Переход в раздел Начинки
    def test_03_chapter_fillings(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        locators = Locators(driver)

        driver.get('https://stellarburgers.nomoreparties.site/')

        locators.get_sign_in_button().click()

        locators.get_input_field_registration_email().send_keys('nadinesmurova0919@yandex.ru')

        locators.get_input_field_registration_password().send_keys('123454321')

        locators.get_login_button().click()

        locators.get_fillings_button().click()

        driver.quit()

section_transitions = SectionTransitions()
section_transitions.test_01_chapter_buns()
section_transitions.test_02_chapter_sauces()
section_transitions.test_03_chapter_fillings()