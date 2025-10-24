import time
from Utilities.ValidatingEmail import *
from selenium.webdriver import ActionChains

from Configurations.Dependencies import *
from Utilities.readProperties import Readconfig
from Utilities.BasePage import BasePage
import re
import pytest

class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    '''---------------Locators---------------------------------'''
    product_click = (By.XPATH, "//a[@href='/products']")
    search_Product_input = (By.XPATH, "//*[@id='search_product']")
    Submit_search_click = (By.XPATH, "//*[@id='submit_search']")
    no_of_product = (By.XPATH, "//*[@class='features_items']/div")
    addtocart_btn = (By.XPATH, "//*[@class='single-products']/div/a")
    addtocart_popup = (By.XPATH, ".//div[@class='product-overlay']//a[contains(@class,'add-to-cart')]")
    continue_shopping_btn_click = (By.XPATH, "//button[normalize-space()='Continue Shopping']")
    btn_addtocart = (By.XPATH, "//li/a[@href='/view_cart']")
    checkout_btn = (By.XPATH, "//a[@class='btn btn-default check_out']")
    Register_login_msg = (By.XPATH, "//p[normalize-space()='Register / Login account to proceed on checkout.']")
    Register_login_popup = (By.XPATH, "//u[normalize-space()='Register / Login']")
    total_cost = (By.XPATH, "//*[@id='cart_info']/table/tbody/tr[last()]/td[4]/p")
    place_order_btn = (By.XPATH, "//a[normalize-space()='Place Order']")
    nameoncard_input = (By.XPATH, "//input[@name='name_on_card']")
    cardnumber_input = (By.XPATH, "//input[@name='card_number']")
    cvv_input = (By.XPATH, "//input[@name='cvc']")
    Expire_MM_input = (By.XPATH, "//input[@placeholder='MM']")
    Expire_YY_input = (By.XPATH, "//input[@placeholder='YYYY']")
    confirm_order_btn = (By.XPATH, "//button[@id='submit']")
    payment_form = (By.XPATH, "//*[@id='payment-form']")
    required_fields = (By.XPATH, "//*[@required]")
    order_confirm_msg = (By.XPATH, "//p[normalize-space()='Congratulations! Your order has been confirmed!']")
    download_invoice_btn = (By.XPATH, "//a[contains(text(),'Download Invoice')]")
    product_container = (By.XPATH, "//div[@class='single-products']")

    """-------------------Actions-----------------------"""
    def click_products(self):
        self.driver.find_element(*self.product_click).click()

    def search_product(self, productname):
        self.driver.find_element(*self.search_Product_input).send_keys(productname)

    def click_searchicon(self):
        self.driver.find_element(*self.Submit_search_click).click()

    def total_numberofproducts(self):
        total = self.driver.find_elements(*self.no_of_product)
        print("Total products found:", len(total))

    def capture_costofproducts(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='single-products']/div/div/h2"))
        )
        return element
    def moveto_addtocart(self, product_element):
        """Hover over product to make overlay visible"""
        product_container = product_element.find_element(By.XPATH, "./ancestor::div[@class='single-products']")
        ActionChains(self.driver).move_to_element(product_container).perform()
        time.sleep(0.5)
        return product_container

    def addtocart_click(self, product_container):
        """Click Add to Cart on overlay using JS (bypass intercepts)"""
        overlay_btn = WebDriverWait(product_container, 10).until(
            lambda d: product_container.find_element(*self.addtocart_btn)
        )
        time.sleep(0.5)  # allow animation to complete
        self.driver.execute_script("arguments[0].click();", overlay_btn)

    def continue_shopping(self):
        self.click(self.driver.find_element(*self.continue_shopping_btn_click))

    def checkout(self):
        self.driver.find_element(*self.btn_addtocart).click()
        self.driver.find_element(*self.checkout_btn).click()

    def empty_cart(self):
        if "Cart is empty!" in self.driver.page_source:
            return False
        return True

    def if_not_registered(self):
        try:
            msg = self.driver.find_element(*self.Register_login_msg).text
            return "Register / Login account" in msg
        except:
            return False

    def Register_popUp(self):
        self.click(self.driver.find_element(*self.Register_login_popup))

    def check_totalammount(self):
        return self.driver.find_element(*self.total_cost).text

    def place_order(self):
        self.click(self.driver.find_element(*self.place_order_btn))
    def payments(self):
        self.driver.find_element(*self.nameoncard_input).send_keys("Pratap")
        cc="1234 5433 5676 7665"
        if cc_number(cc):
            self.driver.find_element(*self.cardnumber_input).send_keys(cc)
        if cvc("123"):
            self.driver.find_element(*self.cvv_input).send_keys("123")
        self.driver.find_element(*self.Expire_MM_input).send_keys("04")
        if year("2030"):
            self.driver.find_element(*self.Expire_YY_input).send_keys("2030")

    def payandconfirm(self):
        self.driver.find_element(*self.confirm_order_btn).click()

    def order_confirm(self):
        return self.driver.find_element(*self.order_confirm_msg).text

    def if_missing_fields(self):
        missing_fields = []
        paymentform = self.driver.find_element(*self.payment_form)
        required_elements = paymentform.find_elements(*self.required_fields)
        for fields in required_elements:
            value = fields.get_attribute("value")
            if not value or value.strip() == "":
                name = fields.get_attribute("name") or fields.get_attribute("id") or "Unknown"
                if name not in missing_fields:
                    missing_fields.append(name)
        return missing_fields

    def download_invoice(self):
        self.driver.find_element(*self.download_invoice_btn).click()
