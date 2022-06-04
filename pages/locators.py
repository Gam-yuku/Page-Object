from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, "[name='registration_submit']") 

    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_HYPERLINK = (By.CSS_SELECTOR, "a[href*='/password-reset/']")
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, "[name='login_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK_INNER_PAGE = (By.XPATH, ('//div[@class="col-sm-6 product_main"]//h1'))
    NAME_BOOK_BASKET_PAGE = (By.XPATH, ('//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]//strong'))
    BAR_ADDED_TO_BASKET = (By.XPATH, ('//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]'))
    PRICE_BOOK = (By.XPATH, ("//p[@class='price_color']"))
    COST_BOOK = (By.XPATH, ('//div[@class="alertinner "]//p//strong'))