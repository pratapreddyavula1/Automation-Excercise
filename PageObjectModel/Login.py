from selenium.common import TimeoutException

from Configurations.Dependencies import *
from Utilities.readProperties import Readconfig
from Utilities.BasePage import BasePage


class LoginPage(BasePage):
    """Page Object for Login functionality."""

    # -------------------- Locators --------------------
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    emailpass_text=(By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")

    # -------------------- Constructor --------------------
    def __init__(self,driver=None):
       super().__init__(driver)

    # -------------------- Actions --------------------
    def click_signup_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK)
        ).click()

    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException


    def enter_email(self, email=None):
        """Enter email in the login field."""
        email =Readconfig.getEmail()
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password=None):
        """Enter password in the password field."""
        password =Readconfig.getpassword()
        pwd_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        pwd_field.clear()
        pwd_field.send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()


    def invalid_email_password(self):
        """
        Check if 'Your email or password is incorrect!' message appears after invalid login.
        Returns True if found, False otherwise.
        """
        try:
            # Wait for message to appear (up to 10s)
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.emailpass_text)
            )

            actual_msg = element.text.strip()
            expected_msg = "Your email or password is incorrect!"

            if actual_msg == expected_msg:
                print("✅ Correct error message displayed.")
                return True
            else:
                print(f"⚠️ Unexpected message: '{actual_msg}'")
                return False

        except TimeoutException:
            print("❌ Error message not found — maybe login worked or locator is wrong.")
            return False

        except Exception as e:
            print(f"⚠️ Exception while validating error message: {e}")
            return False


    def is_login_successful(self):
        """Validate login success by checking the page title."""
        expected_title = "Automation Exercise"
        actual_title = self.driver.title
        if actual_title == expected_title:
            print("✅ Login successful — title matched.")
            return True
        else:
            print(f"❌ Login failed. Expected: '{expected_title}', Got: '{actual_title}'")
            return False