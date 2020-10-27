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
