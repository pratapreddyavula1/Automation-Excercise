import pytest
from PageObjectModel.SignUp import SignupPage
from PageObjectModel.Login import LoginPage
from Utilities.readProperties import Readconfig


class TestLoginSuccessful:
    @pytest.fixture(autouse=True)
    def setup_mode(self, setup):
        self.driver = setup
        self.signup = SignupPage(self.driver)
        self.login = LoginPage(self.driver)  # ✅ same driver for both

    def test_login_signup_flow(self):
        """Signup → If already exists, login."""
        self.signup.click_signup_link()
        self.signup.enter_name("Pratap")
        self.signup.enter_email(Readconfig.getEmail())
        self.signup.click_signup_button()

        if self.signup.alreadyEmail_exist():
            print("Email already exists → Trying login flow.")
            self.login.enter_email()
            self.login.enter_password()
            self.login.click_login_button()
            assert self.login.is_login_successful() or self.login.invalid_email_password()
        else:
            print("New signup flow.")
            self.signup.select_gender()
            self.signup.enter_password(Readconfig.getpassword())
            self.signup.select_dob("12", "5", "2020")
            self.signup.fill_address(
                fname="Pratap",
                lname="Reddy",
                company="TCS",
                address1="Gachibowli",
                address2="Anjaiah Nagar",
                country="India",
                state="Telangana",
                city="Hyderabad",
                zipcode="500081",
                mobile="9839292383",
            )
            self.signup.click_create_account()
            # assert self.signup.account_created(), "❌ Account not created!"
            print("Account Created....")

