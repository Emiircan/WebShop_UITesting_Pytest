import time

from selenium.webdriver.support.ui import Select

from base.page_base import PageBase
from selenium.webdriver.common.by import By


class ShoppingCartPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ADD_TO_CART_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[value='Add to cart']")
    ADD_TO_CART_CONTROL_TEXT_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[class='content']")
    AGREE_BOX_BUTTON_IN_CART_PAGE = (By.CSS_SELECTOR, "[id='termsofservice']")
    CHECK_OUT_BUTTON_IN_CART_PAGE = (By.CSS_SELECTOR, "[id='checkout']")
    BILLING_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='Billing.save()']")
    SHIPPING_ADDRESS_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='Shipping.save()']")
    SHIPPING_METHOD_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='ShippingMethod.save()']")
    PAYMENT_METHOD_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='PaymentMethod.save()']")
    PAYMENT_INFO_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='PaymentInfo.save()']")
    CONFIRM_ORDER_CONTINUE_BUTTON_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[onclick='ConfirmOrder.save()']")
    ORDER_CONTROL_TEXT_IN_PAYMENT_PAGE = (By.CSS_SELECTOR, "[class='title']")

    def click_on_add_to_cart_button_in_product_page(self):
        self.click_element_functionality(self.ADD_TO_CART_IN_PRODUCT_PAGE)

    def successfully_added_to_cart(self):
        self.verify_contains_text_function(self.ADD_TO_CART_CONTROL_TEXT_IN_PRODUCT_PAGE,
                                           "The product has been added to your shopping cart")

    def select_country_in_cart_page(self):
        self.country = Select(self.driver.find_element(By.CSS_SELECTOR, "[id='CountryId']"))
        self.country.select_by_visible_text("Canada")

    def click_on_agree_and_check_out_button(self):
        self.click_element_functionality(self.AGREE_BOX_BUTTON_IN_CART_PAGE)
        self.click_element_functionality(self.CHECK_OUT_BUTTON_IN_CART_PAGE)

    def make_payment_transaction_in_payment_page(self):
        self.click_element_functionality(self.BILLING_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        self.click_element_functionality(self.SHIPPING_ADDRESS_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        self.click_element_functionality(self.SHIPPING_METHOD_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        self.click_element_functionality(self.PAYMENT_METHOD_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        self.click_element_functionality(self.PAYMENT_INFO_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        self.click_element_functionality(self.CONFIRM_ORDER_CONTINUE_BUTTON_IN_PAYMENT_PAGE)
        time.sleep(1)

    def order_placed_successfully(self):
        self.verify_contains_text_function(self.ORDER_CONTROL_TEXT_IN_PAYMENT_PAGE,
                                           "Your order has been successfully processed!")
