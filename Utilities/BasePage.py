# Utilities/BasePage.py
from Configurations.Dependencies import WebDriverWait, EC, Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def select_dropdown(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(value)
