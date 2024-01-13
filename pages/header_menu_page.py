from base.page_base import PageBase
from selenium.webdriver.common.by import By


class HeaderMenu(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    HEADER_MENU_LOGOUT = (By.CSS_SELECTOR, "[class='ico-logout']")
    HEADER_MENU_LOGIN = (By.CSS_SELECTOR, "[class='ico-login']")
    REGISTER_BUTTON_HOMEPAGE = (By.CSS_SELECTOR, "[class='ico-register']")
    HEADER_MENU_WISHLIST_BUTTON = (By.CSS_SELECTOR, "[class='ico-wishlist']")
    HEADER_MENU_SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")

    def click_on_register_button_in_header_menu(self):
        self.click_element_functionality(self.REGISTER_BUTTON_HOMEPAGE)

    def clic_on_log_out_in_header_menu(self):
        self.click_element_functionality(self.HEADER_MENU_LOGOUT)

    def clic_on_log_in_in_header_menu(self):
        self.click_element_functionality(self.HEADER_MENU_LOGIN)

    def clic_on_wishlist_in_header_menu(self):
        self.click_element_functionality(self.HEADER_MENU_WISHLIST_BUTTON)

    def clic_on_shopping_cart_in_header_menu(self):
        self.click_element_functionality(self.HEADER_MENU_SHOPPING_CART_BUTTON)
