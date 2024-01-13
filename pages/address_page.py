from selenium.webdriver.support.ui import Select

from base.page_base import PageBase
from selenium.webdriver.common.by import By


class AddressPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COSTUMER_ADDRESS_IN_HOMEPAGE = (By.CSS_SELECTOR, "[href='/customer/addresses']")
    ADD_NEW_ADDRESS_BUTTON_ADDRESS_PAGE = (By.CSS_SELECTOR, "[value='Add new']")
    FIRST_NAME_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.FirstName']")
    LAST_NAME_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.LastName']")
    EMAIL_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.Email']")
    COUNTRY_SELECT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.CountryId']")
    CITY_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.City']")
    ADDRESS_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.Address1']")
    ZIP_CODE_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.ZipPostalCode']")
    PHONE_NUMBER_INPUT_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[name='Address.PhoneNumber']")
    SAVE_BUTTON_IN_ADDRESS_PAGE = (By.CSS_SELECTOR, "[value='Save']")

    def click_on_address_button_in_homepage(self):
        self.click_element_functionality(self.COSTUMER_ADDRESS_IN_HOMEPAGE)

    def click_on_new_address_button_in_address_page(self):
        self.click_element_functionality(self.ADD_NEW_ADDRESS_BUTTON_ADDRESS_PAGE)

    def enter_on_user_firstname_lastname_email_in_address_page(self):
        self.send_text_functionality(self.FIRST_NAME_INPUT_IN_ADDRESS_PAGE, "Tommy")
        self.send_text_functionality(self.LAST_NAME_INPUT_IN_ADDRESS_PAGE, "Joy")
        self.send_text_functionality(self.EMAIL_INPUT_IN_ADDRESS_PAGE, "tomjoy@gmail.com")

    def enter_on_user_city_address_zipcode_number_in_address_page(self):
        self.send_text_functionality(self.CITY_INPUT_IN_ADDRESS_PAGE, "Houston")
        self.send_text_functionality(self.ADDRESS_INPUT_IN_ADDRESS_PAGE, "Houston street")
        self.send_text_functionality(self.ZIP_CODE_INPUT_IN_ADDRESS_PAGE, "9887")
        self.send_text_functionality(self.PHONE_NUMBER_INPUT_IN_ADDRESS_PAGE, "788 44 54")

    def select_country_in_address_page(self):
        self.country = Select(self.driver.find_element(By.CSS_SELECTOR, "[name='Address.CountryId']"))
        self.country.select_by_visible_text("Canada")

    def click_on_save_button_in_address_page(self):
        self.click_element_functionality(self.SAVE_BUTTON_IN_ADDRESS_PAGE)
