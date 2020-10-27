from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    PROMO = "?promo=newYear2019"

    def add_item_to_busket(self):
        add_bucket = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET_BUTTON)
        add_bucket.click()

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

    def item_price(self):
        page_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_ON_PAGE)
        return page_price.text

    def busket_price_message(self):
        busket_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BUSKET_MESSAGE)
        return busket_price.text

    def check_item_in_busket(self):
        assert self.item_price() == self.busket_price_message(), "Price in Bucket and on Page are not equal!"

    def item_name_on_page(self):
        page_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ON_PAGE)
        return page_book.text

    def item_name_in_busket(self):
        message_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BUSKET_MESSAGE)
        return message_book.text

    def check_item_name_in_access_alert(self):
        assert self.item_name_on_page() == self.item_name_in_busket(), \
            "Name of bock on page and on alert are not equal!"
