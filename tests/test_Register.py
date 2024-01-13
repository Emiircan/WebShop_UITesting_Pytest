import unittest

import pytest
from ddt import data, unpack, ddt

from pages.register_page import RegisterPage
from utilities.ExcelUtility import ExcelUtility
from pages.header_menu_page import HeaderMenu


@pytest.mark.usefixtures("setup")
@ddt
class Test_Register(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.registerpage = RegisterPage(self.driver)
        self.headermenupage = HeaderMenu(self.driver)

    @data(*ExcelUtility.get_data_from_excel("RegisterInfo"))
    @unpack
    def test_new_member_registration(self, firstname, lastname, email, password, cpassword):
        self.headermenupage.click_on_register_button_in_header_menu()
        self.registerpage.enter_on_user_details_in_register_page(firstname=firstname, lastname=lastname, email=email,
                                                                 password=password, cpassword=cpassword)
        self.registerpage.click_on_register_button_in_register_page()
        self.registerpage.user_should_register_successfully()
        self.headermenupage.clic_on_log_out_in_header_menu()

    @data(*ExcelUtility.get_data_from_excel("RegisterInfo"))
    @unpack
    def test_new_member_registration_with_existing_mail(self, firstname, lastname, email, password, cpassword):
        self.headermenupage.click_on_register_button_in_header_menu()
        self.registerpage.enter_on_user_details_in_register_page(firstname=firstname, lastname=lastname, email=email,
                                                                 password=password, cpassword=cpassword)
        self.registerpage.click_on_register_button_in_register_page()
        self.registerpage.user_should_not_register_successfully()
