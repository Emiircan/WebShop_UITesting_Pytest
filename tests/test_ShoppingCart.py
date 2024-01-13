import unittest

import pytest
from ddt import data, ddt, unpack

from pages.login_page import LoginPage
from pages.header_menu_page import HeaderMenu
from pages.wishlist_page import WishlistPage
from pages.shoppingcart_page import ShoppingCartPage
from utilities.ExcelUtility import ExcelUtility


@pytest.mark.usefixtures("setup")
@ddt
class Test_ShoppingCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.wishlistpage = WishlistPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.headermenupage = HeaderMenu(self.driver)
        self.shoppingcartpage = ShoppingCartPage(self.driver)

    @data(*ExcelUtility.get_data_from_excel("Login"))
    @unpack
    def test_login(self, email, password):
        self.headermenupage.clic_on_log_in_in_header_menu()
        self.loginpage.enter_on_user_details_in_login_page(email=email, password=password)
        self.loginpage.click_on_log_in_button_in_login_page()
        self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGOUT, "Log out")

    def test_login_and_complete_your_order(self):
        self.wishlistpage.go_to_mobil_phone_category()
        self.wishlistpage.click_on_smart_phone_in_electronics()
        self.shoppingcartpage.click_on_add_to_cart_button_in_product_page()
        self.shoppingcartpage.successfully_added_to_cart()
        self.headermenupage.clic_on_shopping_cart_in_header_menu()
        self.shoppingcartpage.select_country_in_cart_page()
        self.shoppingcartpage.click_on_agree_and_check_out_button()
        self.shoppingcartpage.make_payment_transaction_in_payment_page()
        self.shoppingcartpage.order_placed_successfully()
