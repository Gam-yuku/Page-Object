from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): # В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера
        assert 'login' in self.browser.current_url, 'ссылка не содержит "login"'   

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "email input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_HYPERLINK), "hyperlink 'I forgot password' input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BTN), "login submit button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "password input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "repeated password input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BTN), "registration submit button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN).click()      
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCES), "'Registration message' is not presented"