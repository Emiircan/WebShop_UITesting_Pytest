from base.page_base import PageBase
from selenium.webdriver.common.by import By


class LoginPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_PAGE_EMAIL_INPUT = (By.CSS_SELECTOR, "[class='email']")
    LOGIN_PAGE_PASSWORD_INPUT = (By.CSS_SELECTOR, "[class='password']")
    LOGIN_PAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, "[class='button-1 login-button']")
    LOGIN_PAGE_ERROR_MESSAGE = (By.CSS_SELECTOR, "[class='validation-summary-errors']")

    def enter_on_user_details_in_log_in_page(self, scenario_type, email, password):
        self.send_text_functionality(self.LOGIN_PAGE_EMAIL_INPUT, email)
        self.send_text_functionality(self.LOGIN_PAGE_PASSWORD_INPUT, password)

    def enter_on_user_details_in_login_page(self, email, password):
        self.send_text_functionality(self.LOGIN_PAGE_EMAIL_INPUT, email)
        self.send_text_functionality(self.LOGIN_PAGE_PASSWORD_INPUT, password)

    def click_on_log_in_button_in_login_page(self):
        self.click_element_functionality(self.LOGIN_PAGE_LOGIN_BUTTON)
