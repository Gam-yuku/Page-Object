from selenium.webdriver.common.by import By
from pages.product_page import ProductPage #если модуль из другой папки - весь путь
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

urls = [f"{product_base_link}/?promo=offer{no}" if no !=7 else pytest.param(f"{product_base_link}/?promo=offer{no}", marks=pytest.mark.xfail(reason="some bug")) for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.adding_to_basket()          #Нажимаем на кнопку "Добавить в корзину".
    page.solve_quiz_and_get_code()   # Посчитать результат математического выражения и ввести ответ
    page.should_be_in_basket()       # Ожидаемый результат (сообщение, название, стоимость, цена) pytest -s -v --language=en test_product_page.py # --tb=line  
 
"""
@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])
"""