# POM/logout_page.py

from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logout_link = (By.XPATH, "//a[normalize-space()='Logout']")  # change XPATH based on your app

    def perform_logout(self):
        try:
            self.driver.find_element(*self.logout_link).click()
            print("👋 Logged out successfully")
        except Exception as e:
            print(f"❌ Logout failed: {e}")
