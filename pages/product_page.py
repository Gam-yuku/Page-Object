from .base_page import BasePage #если модуль из той же папки указывается точка
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage): 
    def adding_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        login_link.click()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def should_be_in_basket(self):
        self.message_added_to_basket()
        self.cost_basket_equals_price_product()
    def message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BAR_ADDED_TO_BASKET), "Нет сообщения о том, что товар добавлен в корзину"
        assert (self.browser.find_element(*ProductPageLocators.NAME_BOOK_INNER_PAGE)).text == (self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET_PAGE)).text, "Название товара в сообщении не совпадает с добавленным товаром"
    def cost_basket_equals_price_product(self):
        assert self.is_element_present(*ProductPageLocators.COST_BOOK), "Нет сообщения со стоимостью корзины"
        assert (self.browser.find_element(*ProductPageLocators.COST_BOOK)).text==(self.browser.find_element(*ProductPageLocators.PRICE_BOOK)).text, "Стоимость корзины и цена совпадают"
        
    """
    Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
    """






