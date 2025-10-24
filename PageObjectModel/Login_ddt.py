from selenium.common import TimeoutException

from Configurations.Dependencies import *
from Utilities.readProperties import Readconfig
from Utilities.ExcelUtilities import *



class LoginPage_DDT:
    """Page Object for Login functionality."""

    # -------------------- Locators --------------------
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    emailpass_text = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")

    # -------------------- Constructor --------------------
    def __init__(self, driver):
        self.driver = driver

    # -------------------- Actions --------------------
    def click_signup_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK)
        ).click()


    def enter_email(self, email=None):
        """Enter email in the login field."""
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password=None):
        """Enter password in the password field."""
        pwd_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        pwd_field.clear()
        pwd_field.send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def is_valid_login(self):
        if self.driver.title == "Automation Exercise":
            print("✅ Login successful — title matched.")
            return True
        else:
            return False

