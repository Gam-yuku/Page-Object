from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, "[name='registration_submit']") 
    REGISTRATION_SUCCES = (By.XPATH, "//div[@class='alert alert-success  fade in']")

    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_HYPERLINK = (By.CSS_SELECTOR, "a[href*='/password-reset/']")
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, "[name='login_submit']")

class ProductPageLocators():
    INNER_PAGE_BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    INNER_PAGE_NAME_BOOK = (By.XPATH, ('//div[@class="col-sm-6 product_main"]//h1'))
    INNER_PAGE_PRICE_BOOK = (By.XPATH, ("//p[@class='price_color']"))

    BASKET_PAGE_NAME_BOOK = (By.XPATH, ('//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]//strong'))
    BASKET_PAGE_SUCCESS_MESSAGE = (By.XPATH, ('//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]'))
    BASKET_PAGE_COST_BOOK = (By.XPATH, ('//div[@class="alertinner "]//p//strong'))

class BasketPageLocators():
    BASKET_BTN = (By.XPATH, '//a[@class="btn btn-default"]')
    BASKET_PAGE_BOOKS_IN_BASKET = (By.XPATH, '//div[@class="basket-items"]')
    BASKET_PAGE_TEXT_EMPTY_BASKET = (By.XPATH, '//div[@id="content_inner"]/p[text()]')


