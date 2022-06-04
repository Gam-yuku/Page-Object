from selenium.webdriver.common.by import By
from pages.main_page import MainPage #если модуль из другой папки - весь путь
from pages.login_page1 import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина, pytest --language=en test_main_page.py
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  
      


"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link) #page.open()   
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link") #page.go_to_login_page()
    login_link.click() #pytest -v --tb=line --language=en test_main_page.py

"""