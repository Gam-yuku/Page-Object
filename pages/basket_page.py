from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage): 
    def go_to_basket(self):
        (self.browser.find_element(*BasketPageLocators.BASKET_BTN)).click()
    def no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PAGE_BOOKS_IN_BASKET), \
        "'Items' is presented but should not be"
    def message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PAGE_TEXT_EMPTY_BASKET), \
        "No message - 'Your basket is empty'"  
