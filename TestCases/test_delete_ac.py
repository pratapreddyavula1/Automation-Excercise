import pytest
from PageObjectModel.Login import *
from Utilities.ExcelUtilities import *
from PageObjectModel.Login_ddt import *


class TestLogout:
    @pytest.fixture(autouse=True)
    def setup_mode(self,setup):
        self.driver=setup
        self.login=LoginPage(self.driver)

    def test_logout(self):
        self.login.click_signup_login()
        self.login.enter_email()
        self.login.enter_password()
        self.login.click_login_button()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()
        print("Account Delete  Successfully...........")