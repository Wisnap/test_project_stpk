from .pages.product_page import ProductPage


link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{ProductPage.PROMO}'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_busket()
    page.solve_quiz_and_get_code()
    page.check_item_in_busket()
    page.check_item_name_in_access_alert()



