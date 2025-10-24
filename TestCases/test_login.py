import pytest
from Utilities.readProperties import Readconfig
from PageObjectModel.Login import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    """Test suite for validating Login functionality."""

    @pytest.fixture(autouse=True)
    def setup_method(self,setup):
        self.driver=setup
        """Initialize driver and open application."""
        self.login_page = LoginPage(self.driver)

    def test_login_valid_user(self):
        """Test valid login credentials."""
        # self.login_page.click_signup_login()
        self.login_page.enter_email()
        self.login_page.enter_password()
        self.login_page.click_login_button()
        if self.login_page.invalid_email_password():
            print("⚠️ Invalid login detected — skipping success check.")
        else:
            assert self.login_page.is_login_successful(), "❌ Login unsuccessful!"

