from .base_page import BasePage #если модуль из той же папки указывается точка
# from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page1 import LoginPage

class MainPage(BasePage): #заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

"""
class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) #вернуть объект, чтобы осуществить переход к странице login page (для работы с
        #ним в test_main_page)
        #при создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # def go_to_login_page1(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
"""