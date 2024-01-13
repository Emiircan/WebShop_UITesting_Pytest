from base.page_base import PageBase
from selenium.webdriver.common.by import By


class RegisterPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    REGISTER_PAGE_FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[id='FirstName']")
    REGISTER_PAGE_LAST_NAME_INPUT = (By.CSS_SELECTOR, "[id='LastName']")
    REGISTER_PAGE_EMAIL_INPUT = (By.CSS_SELECTOR, "[id='Email']")
    REGISTER_PAGE_PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='Password']")
    REGISTER_PAGE_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='ConfirmPassword']")
    REGISTER_PAGE_REGISTER_BUTTON = (By.CSS_SELECTOR, "[id='register-button']")
    REGISTER_PAGE_REGISTER_CONTROL_TEXT = (By.CSS_SELECTOR, "div[class='result']")
    REGISTER_PAGE_ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='validation-summary-errors']")

    def enter_on_user_details_in_register_page(self, firstname, lastname, email, password, cpassword):
        self.send_text_functionality(self.REGISTER_PAGE_FIRST_NAME_INPUT, firstname)
        self.send_text_functionality(self.REGISTER_PAGE_LAST_NAME_INPUT, lastname)
        self.send_text_functionality(self.REGISTER_PAGE_EMAIL_INPUT, email)
        self.send_text_functionality(self.REGISTER_PAGE_PASSWORD_INPUT, password)
        self.send_text_functionality(self.REGISTER_PAGE_CONFIRM_PASSWORD_INPUT, cpassword)

    def click_on_register_button_in_register_page(self):
        self.click_element_functionality(self.REGISTER_PAGE_REGISTER_BUTTON)

    def user_should_register_successfully(self):
        self.verify_contains_text_function(self.REGISTER_PAGE_REGISTER_CONTROL_TEXT, "Your registration completed")

    def user_should_not_register_successfully(self):
        self.verify_contains_text_function(self.REGISTER_PAGE_ERROR_MESSAGE, "The specified email already exists")
