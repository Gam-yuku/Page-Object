from selenium.webdriver.common.by import By
from pages.main_page import MainPage #если модуль из другой папки - весь путь
from pages.login_page1 import LoginPage
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    
    page.go_to_login_page()         
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  
      
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open() 
    page.go_to_basket()
    page.no_items_in_the_cart()
    page.message_empty_basket()