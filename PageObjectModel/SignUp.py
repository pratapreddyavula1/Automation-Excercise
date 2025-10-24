import pytest

from Configurations.Dependencies import WebDriverWait,EC,Select,By
from Utilities.readProperties import Readconfig
from Utilities.BasePage import BasePage



class SignupPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    # Locators
    signup_link = (By.XPATH, "//a[normalize-space()='Signup / Login']") #//a[normalize-space()='Signup / Login']
    name_input = (By.XPATH, "//*[@name='name']")
    email_input = (By.XPATH, "//*[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    gender_radio = (By.XPATH, "//input[@id='id_gender1']")
    password_input = (By.XPATH, "//input[@id='password']")
    day_select = (By.XPATH, "//*[@id='days']")
    month_select = (By.ID,"months")
    year_select = (By.XPATH, "//*[@id='years']")
    first_name_input = (By.XPATH, "//*[@id='first_name']")
    last_name_input = (By.XPATH, "//*[@id='last_name']")
    company_input = (By.XPATH, "//*[@id='company']")
    address1_input = (By.XPATH, "//*[@data-qa='address']")
    address2_input = (By.XPATH, "//*[@data-qa='address2']")
    country_select = (By.XPATH, "//*[@data-qa='country']")
    state_input = (By.XPATH, "//*[@data-qa='state']")
    city_input = (By.XPATH, "//*[@data-qa='city']")
    zipcode_input = (By.XPATH, "//*[@data-qa='zipcode']")
    mobile_input = (By.XPATH, "//*[@data-qa='mobile_number']")
    create_account_button = (By.XPATH, "//*[@data-qa='create-account']")
    text_Ac_created=(By.XPATH,"//*[contains(text(),'Automation Exercise - Account Created')]")
    text_exist_email=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/p")
    continue_button=(By.XPATH,"//a[@class='btn btn-primary']")


    # Actions
    def click_signup_link(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.signup_link)).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_signup_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.signup_button)).click()


    def select_gender(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.gender_radio)).click()

    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def select_dob(self, day, month, year):
        Select(self.driver.find_element(*self.day_select)).select_by_value(day)
        Select(self.driver.find_element(*self.month_select)).select_by_value(month)
        Select(self.driver.find_element(*self.year_select)).select_by_value(year)

    def fill_address(self, fname, lname, company, address1, address2, country, state, city, zipcode, mobile):
        self.driver.find_element(*self.first_name_input).send_keys(fname)
        self.driver.find_element(*self.last_name_input).send_keys(lname)
        self.driver.find_element(*self.company_input).send_keys(company)
        self.driver.find_element(*self.address1_input).send_keys(address1)
        self.driver.find_element(*self.address2_input).send_keys(address2)
        Select(self.driver.find_element(*self.country_select)).select_by_visible_text(country)
        self.driver.find_element(*self.state_input).send_keys(state)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.zipcode_input).send_keys(zipcode)
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def click_create_account(self):
        self.driver.find_element(*self.create_account_button).click()

    def alreadyEmail_exist(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(self.text_exist_email))
            msg = element.text.strip()

            return msg
        except:
            return False



    def account_created(self):
        try:
            ac=self.driver.find_element(self.text_Ac_created).text
            if ac=="Automation Exercise - Account Created":
                return True

        except Exception as e:
            print(e)
            return False

    #validate any required fields missing/not  Using Javascript
    # invalid_fields = self.driver.execute_script("return Array.from(document.querySelectorAll(':invalid'));")
    def get_missing_required_fields(self):
        """
        Return list of empty required fields inside the signup form.
        Checks:
        1. Input fields with HTML 'required' attribute
        2. Input fields associated with labels containing '*'
        """
        missing_fields = []

        # Locate signup form container
        signup_form = self.driver.find_element(By.ID, "form")  # Adjust if your form has different ID

        # 1️⃣ Fields with 'required' attribute inside signup form
        required_elements = signup_form.find_elements(By.XPATH, ".//*[@required]")
        for field in required_elements:
            value = field.get_attribute("value")
            if not value or value.strip() == "":
                name = field.get_attribute("name") or field.get_attribute("id") or "Unknown"
                if name not in missing_fields:
                    missing_fields.append(name)

        # 2️⃣ Labels with '*' inside signup form
        labels = signup_form.find_elements(By.XPATH, ".//label[contains(text(), '*')]")
        for label in labels:
            for_attr = label.get_attribute("for")
            if for_attr:
                try:
                    input_field = signup_form.find_element(By.ID, for_attr)
                    value = input_field.get_attribute("value")
                    if not value or value.strip() == "":
                        name = input_field.get_attribute("name") or input_field.get_attribute("id") or "Unknown"
                        if name not in missing_fields:
                            missing_fields.append(name)
                except:
                    continue

        return missing_fields

    def continue_btn(self):
        self.driver.find_element(*self.continue_button).click()
    def title(self):
       return self.driver.title



    # def validate_mandatory_fields(self):
    #     try:
    #         invalid_field=self.driver.execute_script("return document.querySelector(':invaild';")
    #         if invalid_field:
    #             field_name=(
    #                 invalid_field.get_attribute('name')
    #                 or invalid_field.get_attribute('id')
    #                 or invalid_field.get_attribute('placeholder')
    #                 or "Unknown field"
    #             )
    #             pytest.fail(f"⚠️ Required field missing or invalid: {field_name}")
    #         else:
    #             print("✅ All required fields are filled correctly.")
    #     except Exception as e:
    #         pytest.fail(f"Error while validating required fields: {e}")