import unittest

import pytest
from ddt import data, unpack, ddt

from pages.login_page import LoginPage
from pages.header_menu_page import HeaderMenu
from pages.wishlist_page import WishlistPage
from utilities.ExcelUtility import ExcelUtility


@pytest.mark.usefixtures("setup")
@ddt
class Test_Wishlist(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.loginpage = LoginPage(self.driver)
        self.headermenupage = HeaderMenu(self.driver)
        self.wishlistpage = WishlistPage(self.driver)

    @data(*ExcelUtility.get_data_from_excel("Login"))
    @unpack
    def test_login(self, email, password):
        self.headermenupage.clic_on_log_in_in_header_menu()
        self.loginpage.enter_on_user_details_in_login_page(email=email, password=password)
        self.loginpage.click_on_log_in_button_in_login_page()
        self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGOUT, "Log out")

    def test_login_and_add_to_product_in_wishlist(self):
        self.wishlistpage.go_to_mobil_phone_category()
        self.wishlistpage.click_on_smart_phone_in_electronics()
        self.wishlistpage.click_on_add_wishlist_button_in_product_page()
        self.wishlistpage.successfully_added_to_wishlist()
        self.headermenupage.clic_on_wishlist_in_header_menu()
        self.wishlistpage.clear_wishlist_list()
        self.wishlistpage.successfully_cleared_wishlist()
