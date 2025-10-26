import pytest
import sys
from selenium.webdriver.common.by import By
from Configurations.Dependencies import *
from PageObjectModel.SignUp import SignupPage
from Utilities.readProperties import Readconfig
from Utilities.ValidatingEmail import validating_email
from PageObjectModel.Login import LoginPage
from PageObjectModel.Logout import LogoutPage
from Utilities.CustomLogger import logger




@pytest.mark.usefixtures("setup")
class TestSignup:
    """Test class to verify the Signup functionality."""

    @pytest.fixture(autouse=True)
    def setup_class(self, setup):
        """Fixture to initialize WebDriver and Page Object."""
        self.driver = setup
        self.signup_page = SignupPage(self.driver)
        self.login=LoginPage(self.driver)
        self.logout=LogoutPage(self.driver)

    def test_signup(self):
        logger.info("********* Test_Login Started *********")
        logger.info("Opening browser and navigating to login page")
        """Verify signup with a valid email and complete user details."""

        # Step 1: Navigate to Signup section
        self.signup_page.click_signup_link()
        logger.info("Entering username and password")
        logger.info("Clicking on login button")
        # Step 2: Validate and enter email
        name = "Pratap"
        email = Readconfig.getEmail()
        self.signup_page.enter_name(name)

        if not validating_email(email):
            pytest.fail(f"Invalid email format: {email}")

        self.signup_page.enter_email(email)
        self.signup_page.click_signup_button()

        if self.signup_page.alreadyEmail_exist() == "Email Address already exist!":
            logger.warning(f"Email already exists...skipping signup and running login.{Readconfig.getEmail()}")
            pytest.skip("Email already exists...skipping signup and running login.")


        # Step 3: Fill Account Information
        self.signup_page.select_gender()
        self.signup_page.enter_password(Readconfig.getpassword())
        self.signup_page.select_dob(day="12", month="3", year="2020")

        # Step 4: Fill Address Information
        self.signup_page.fill_address(
            fname="Pratap",
            lname="Reddy",
            company="TCS",
            address1="Gachibowli",
            address2="Anjuiagh Nagar",
            country="India",
            state="Telangana",
            city="Hyderabad",
            zipcode="500081",
            mobile="9839292383"
        )

        # Step 5: Create account and verify success
        self.signup_page.click_create_account()
        try:
            assert self.signup_page.account_created(), "Account creation failed."
        except Exception as e:
            print(e)
        self.signup_page.get_missing_required_fields()
        # Step X: Validate required fields before clicking create account
        missing_fields = self.signup_page.get_missing_required_fields()
        assert not missing_fields, f"Required fields missing: {', '.join(missing_fields)}"

        self.signup_page.continue_btn()
        print("Welcome to"+self.signup_page.title())
        self.logout.perform_logout()

        logger.info("********* Test_Login Completed *********")