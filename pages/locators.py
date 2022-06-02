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

