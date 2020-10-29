from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BUCKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK_ON_PAGE = (By.XPATH, "//h1")
    NAME_BOOK_IN_BUSKET_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRICE_OF_BOOK_ON_PAGE = (By.XPATH, "//p[@class='price_color']")
    PRICE_OF_BOOK_IN_BUSKET_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")


class LoginPageLocators():
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_END_REGISTRATION = (By.CSS_SELECTOR, "button[name='registration_submit']")


class BasketPageLocators():
    ITEMS_TO_BUY_ELEMENT = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BUSKET_EMPTY_TEXT = (By.XPATH, "//div[@class='content']/div[2]/p")
