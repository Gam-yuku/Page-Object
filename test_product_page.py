from selenium.webdriver.common.by import By
from pages.product_page import ProductPage #если модуль из другой папки - весь путь
import pytest
from pages.base_page import BasePage #если модуль из другой папки - весь путь
from pages.basket_page import BasketPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" if no !=7 else pytest.param(f"{product_base_link}/?promo=offer{no}", marks=pytest.mark.xfail(reason="some bug")) for no in range(10)]
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open()                     
    page.adding_to_basket()         
    page.solve_quiz_and_get_code()   
    page.should_be_in_basket()       # Ожидаемый результат (сообщение, название, стоимость, цена) pytest -s -v --language=en test_product_page.py # --tb=line  
 
"""
@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])
                                  pytest -s -v --language=en  test_product_page.py::test_guest_can_add_product_to_basket
"""
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'
    page = ProductPage(browser, link) 
    page.open()                         
    page.adding_to_basket() 
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'
    page = ProductPage(browser, link) 
    page.open()                         
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'
    page = ProductPage(browser, link) 
    page.open()                         
    page.adding_to_basket() 
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.no_items_in_the_cart()
    page.message_empty_basket()
