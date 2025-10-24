from selenium.webdriver import ActionChains

from PageObjectModel.Login import LoginPage
from PageObjectModel.Product_Purchase import Product
import pytest
import re
from Configurations.Dependencies import *
from Utilities.ValidatingEmail import *
class Test_pageProduct:
    @pytest.fixture(autouse=True)
    def setup_mode(self, setup):
        self.driver = setup
        self.login = LoginPage(self.driver)
        self.product = Product(self.driver)

    def test_productpage(self):
        """Login"""
        # self.login.click_signup_login()
        # self.login.enter_email()
        # self.login.enter_password()
        # self.login.click_login_button()
        # self.login.is_login_successful()

        """Product flow"""
        self.product.click_products()
        self.product.search_product("tshirt")
        self.product.click_searchicon()


        """capturing Product which price <=1000 Prices"""

        for element in self.product.capture_costofproducts():
            text = element.get_attribute("innerText").strip()  # remove extra spaces/newlines

            # Remove currency and extract digits
            match = re.search(r'(\d+)',text)
            if match:
                price = int(match.group())
                if price <= 1000:
                    product_container = self.product.moveto_addtocart(element)
                    self.product.addtocart_click(product_container)
                    self.product.continue_shopping()



        """Checkout"""
        self.product.checkout()
        if self.product.if_not_registered():
            self.product.Register_popUp()
            self.login.enter_email()
            self.login.enter_password()
            self.login.click_login_button()
            self.login.is_login_successful()

        """Order & Payment"""
        # print("Total amount:", self.product.check_totalammount())
        self.product.place_order()
        self.product.payments()
        self.product.payandconfirm()

        if self.product.order_confirm() != 'Congratulations! Your order has been confirmed!':
            missing = self.product.if_missing_fields()
            pytest.fail(f"❌ Order confirmation failed. Missing fields: {missing}")
        else:
            self.product.download_invoice()
            print("🎉 You purchased products successfully!")
