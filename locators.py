from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

locators = {
    # Кнопка "Личный кабинет"
    'personal_account_button': {
        'by': By.LINK_TEXT,
        'text': "Личный Кабинет"
    },

    # Ссылка "Зарегистироваться"
    'registration_link': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/div/p[1]/a'
    },

    # Поле ввода "Имя"
    'input_field_name': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    },

    # Поле ввода "Email"
    'input_field_email': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    },

    # Поле ввода "Пароль"
    'input_field_password': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    },

    # Кнопка "Зарегистрироваться"
    'registration_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/button'
    },

    # Кнопка "Войти в аккаунт"
    'sign_in_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/section[2]/div/button'
    },

    # Поле ввода регистрации "Email"
    'input_field_registration_email': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    },

    # Поле ввода регистрации "Пароль"
    'input_field_registration_password': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    },

    # Кнока "Войти"
    'login_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/form/button'
    },

    # Ссылка "Войти"
    'login_link': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/div/p/a'

    },

    # Ссылка "Востановить пароль"
    'restore_password_link': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/div/p[2]/a'
    },

    # Кнопка "Конструктор"
    'button_constructor': {
        'by': By.LINK_TEXT,
        'text': 'Конструктор'
    },

    # Логотип
    'logo': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/header/nav/a/p'
    },

    # Кнопка "Выйти"
    'exit_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    },
    # Кнопка "Булки"
    'buns_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'
    },
    # Кнопка "Соусы"
    'sauce_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span'
    },
    # Кнопка "Начинки"
    'fillings_button': {
        'by': By.XPATH,
        'text': '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span'
    }
}


class Locators:
    def __init__(self, driver):
        self._driver = driver

    def get(self, name):
        return WebDriverWait(self._driver, 3).until(expected_conditions.presence_of_element_located(
            (locators.get(name).get('by'), locators.get(name).get('text'))))

    def get_personal_account_button(self):
        return self.get('personal_account_button')

    def get_registration_link(self):
        return self.get('registration_link')

    def get_input_field_name(self):
        return self.get('input_field_name')

    def get_input_field_email(self):
        return self.get('input_field_email')

    def get_input_field_password(self):
        return self.get('input_field_password')

    def get_registration_button(self):
        return self.get('registration_button')

    def get_sign_in_button(self):
        return self.get('sign_in_button')

    def get_input_field_registration_email(self):
        return self.get('input_field_registration_email')

    def get_input_field_registration_password(self):
        return self.get('input_field_registration_password')

    def get_login_button(self):
        return self.get('login_button')

    def get_login_link(self):
        return self.get('login_link')

    def get_restore_password_link(self):
        return self.get('restore_password_link')

    def get_button_constructor(self):
        return self.get('button_constructor')

    def get_logo(self):
        return self.get('logo')

    def get_exit_button(self):
        return self.get('exit_button')

    def get_buns_button(self):
        return self.get('buns_button')

    def get_sauce_button(self):
        return self.get('sauce_button')

    def get_fillings_button(self):
        return self.get('fillings_button')
