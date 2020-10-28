import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.login_page import BasePage
from selenium import webdriver
import faker
import time

# link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{ProductPage.PROMO}'
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                               pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                           "/?promo=offer7",
#                                          marks=pytest.mark.xfail),
#                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):


@pytest.mark.smoke
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user(f.email(), "strongPassWordd")
        self.page.open()
        self.page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        self.page = ProductPage(browser, link)
        self.page.add_item_to_busket()

    def test_user_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, link)
        self.page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_busket()
    page.solve_quiz_and_get_code()
    page.check_item_name_in_access_alert()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_busket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_busket()
    page.solve_quiz_and_get_code()
    page.should_dissapeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
