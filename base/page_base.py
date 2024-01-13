from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def send_text_functionality(self, locator, value):
        self.wait_until_element_visibility(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click_element_functionality(self, locator):
        self.wait_until_element_to_be_clickable(locator)
        element = self.driver.find_element(*locator)
        element.click()

    def get_element_text(self, locator):
        self.wait_until_element_to_be_located(locator)
        element = self.driver.find_element(*locator)
        return element.text

    def verify_contains_text_function(self, locator, excepted):
        element_text = self.get_element_text(locator)
        assert element_text.lower().__contains__(excepted.lower())

    def wait_until_element_visibility(self, locator):
        self.wait.until(EC.visibility_of(self.driver.find_element(*locator)))

    def wait_until_element_to_be_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_until_element_to_be_located(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
