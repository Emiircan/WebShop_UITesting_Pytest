from base.page_base import PageBase
from selenium.webdriver.common.by import By


class WishlistPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ELECTRONIC_HOVER_IN_HOMEPAGE = (By.CSS_SELECTOR, "[href='/electronics']")
    CELL_PHONE_IN_HOMEPAGE = (By.XPATH, "(//*[@href='/cell-phones']) [4]")
    SMART_PHONE_IN_HOMEPAGE = (By.CSS_SELECTOR, "[class='product-title']")
    ADD_WISHLIST_BUTTON_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[value='Add to wishlist']")
    ADD_WISHLIST_CONTROL_TEXT_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[class='content']")
    REMOVE_BOX_IN_WISHLIST_PAGE = (By.CSS_SELECTOR, "[name='removefromcart']")
    UPDATE_WISHLIST_BUTTON_IN_WISHLIST_PAGE = (By.CSS_SELECTOR, "[value='Update wishlist']")
    WISHLIST_CONTROL_TEXT_IN_WISHLIST_PAGE = (By.CSS_SELECTOR, "[class='wishlist-content']")

    def go_to_mobil_phone_category(self):
        self.click_element_functionality(self.ELECTRONIC_HOVER_IN_HOMEPAGE)
        self.click_element_functionality(self.CELL_PHONE_IN_HOMEPAGE)

    def click_on_smart_phone_in_electronics(self):
        self.click_element_functionality(self.SMART_PHONE_IN_HOMEPAGE)

    def click_on_add_wishlist_button_in_product_page(self):
        self.click_element_functionality(self.ADD_WISHLIST_BUTTON_IN_PRODUCT_PAGE)

    def successfully_added_to_wishlist(self):
        self.verify_contains_text_function(self.ADD_WISHLIST_CONTROL_TEXT_IN_PRODUCT_PAGE,
                                           "The product has been added to your wishlist")

    def clear_wishlist_list(self):
        self.click_element_functionality(self.REMOVE_BOX_IN_WISHLIST_PAGE)
        self.click_element_functionality(self.UPDATE_WISHLIST_BUTTON_IN_WISHLIST_PAGE)

    def successfully_cleared_wishlist(self):
        self.verify_contains_text_function(self.WISHLIST_CONTROL_TEXT_IN_WISHLIST_PAGE, "The wishlist is empty!")
