import unittest

import pytest
from ddt import data, ddt, unpack

from pages.address_page import AddressPage
from pages.login_page import LoginPage
from pages.header_menu_page import HeaderMenu
from utilities.ExcelUtility import ExcelUtility


@pytest.mark.usefixtures("setup")
@ddt
class Test_Address(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.addresspage = AddressPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.headermenupage = HeaderMenu(self.driver)

    @data(*ExcelUtility.get_data_from_excel("Login"))
    @unpack
    def test_login(self, email, password):
        self.headermenupage.clic_on_log_in_in_header_menu()
        self.loginpage.enter_on_user_details_in_login_page(email=email, password=password)
        self.loginpage.click_on_log_in_button_in_login_page()
        self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGOUT, "Log out")

    def test_login_and_create_address_record(self):
        self.addresspage.click_on_address_button_in_homepage()
        self.addresspage.click_on_new_address_button_in_address_page()
        self.addresspage.enter_on_user_firstname_lastname_email_in_address_page()
        self.addresspage.select_country_in_address_page()
        self.addresspage.enter_on_user_city_address_zipcode_number_in_address_page()
        self.addresspage.click_on_save_button_in_address_page()
