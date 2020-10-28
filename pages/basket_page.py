from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_basket_element_present(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_ELEMENT), \
            "Item header is presented, but should not be"

    def should_be_empty_text_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BUSKET_EMPTY_TEXT), \
            "Empty busket message is presented"



