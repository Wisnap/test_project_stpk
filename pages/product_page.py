from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    PROMO = "?promo=newYear"

    def add_item_to_bucket(self):
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

    def check_item_in_bucket(self):
        bucket_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BUCKET_MESSAGE)
        page_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_ON_PAGE)
        print(bucket_price)
        print(page_price)
        assert bucket_price.text == page_price.text, "Price in Bucket and on Page are not equal!"

    def check_item_name_in_bucket(self):
        page_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ON_PAGE)
        message_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BUCKET_MESSAGE)
        assert page_book.text == message_book.text, "Name of bock on page and on alert are not equal!"
