from selenium.webdriver.common.by import By
from pages.login_page1 import LoginPage #если модуль из другой папки - весь путь

def test_guest_should_use_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form() #pytest -v --tb=line --language=en test_login_page.py