import unittest

import pytest
from ddt import data, unpack, ddt

from pages.login_page import LoginPage
from pages.header_menu_page import HeaderMenu
from utilities.ExcelUtility import ExcelUtility


@pytest.mark.usefixtures("setup")
@ddt
class Test_Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.headermenupage = HeaderMenu(self.driver)
        self.loginpage = LoginPage(self.driver)

    @data(*ExcelUtility.get_data_from_excel("LoginInfo"))
    @unpack
    def test_login_with_in_valid_mail(self, scenario_type, email, password):
        if scenario_type == "invalid_email":
            self.headermenupage.clic_on_log_in_in_header_menu()
            self.loginpage.enter_on_user_details_in_log_in_page(scenario_type=scenario_type, email=email,
                                                                password=password)
            self.loginpage.click_on_log_in_button_in_login_page()
            self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGIN, "Log in")

        elif scenario_type == "invalid_password":
            self.headermenupage.clic_on_log_in_in_header_menu()
            self.loginpage.enter_on_user_details_in_log_in_page(scenario_type=scenario_type, email=email,
                                                                password=password)
            self.loginpage.click_on_log_in_button_in_login_page()
            self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGIN, "Log in")

        elif scenario_type == "valid":
            self.headermenupage.clic_on_log_in_in_header_menu()
            self.loginpage.enter_on_user_details_in_log_in_page(scenario_type=scenario_type, email=email,
                                                                password=password)
            self.loginpage.click_on_log_in_button_in_login_page()
            self.headermenupage.verify_contains_text_function(self.headermenupage.HEADER_MENU_LOGOUT, "Log out")
