import pytest
from PageObjectModel.Login import *
from Utilities.ExcelUtilities import *
from PageObjectModel.Login_ddt import *


class TestLogin_ddt:
    @pytest.fixture(autouse=True)
    def setup_mode(self,setup):
        self.driver=setup
        self.login=LoginPage_DDT(self.driver)

    """
    Testcase for Login Functionality using Data Driven Testing 
    """

    def test_login_ddt(self):
        file = Readconfig.xlfilename()

        """ Data Driven testing"""

        rows=ExcelUtils.get_rows(file)
        for r in range(2, rows + 1):
            email = ExcelUtils.read_data(file, r, 1)
            password = ExcelUtils.read_data(file, r, 2)

            # Always reset session for clean state
            self.driver.delete_all_cookies()
            self.driver.get(Readconfig.getURL())

            # Wait until the Signup/Login link is visible before proceeding
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Signup / Login']"))
            )

            # Perform login steps
            self.login.click_signup_login()
            self.login.enter_email(email)
            self.login.enter_password(password)
            self.login.click_login_button()

            # Validate result
            actual_status = self.login.is_valid_login()

            if actual_status:
                ExcelUtils.write_data(file, r, 4, "PASS")
                ExcelUtils.green_color(file, r, 4)
                print(f"✅ Login passed for user: {email}")
            else:
                ExcelUtils.write_data(file, r, 4, "FAIL")
                ExcelUtils.red_color(file, r, 4)
                print(f"❌ Login failed for user: {email}")

        """Parameterization
        """

    @pytest.mark.parametrize("email,password,expected", [
        ("abc.1@gmail.com", "abc@123", "PASS"),
        ("invalid_user@gmail.com", "wrongpass", "FAIL"),
        ("", "blankpass", "FAIL"),
    ])
    def test_login_param(self, email, password, expected):
        """Parameterized login test"""
        self.driver.delete_all_cookies()
        self.driver.get(Readconfig.getURL())

        self.login.click_signup_login()
        self.login.enter_email(email)
        self.login.enter_password(password)
        self.login.click_login_button()

        actual = "PASS" if self.login.is_valid_login() else "FAIL"

        assert actual == expected, f"Expected {expected}, got {actual}"