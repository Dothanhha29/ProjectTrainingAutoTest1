from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):
    """By locator"""
    SIGNIN_BUTTON = (By.CLASS_NAME, 'login')
    EMAIL = (By.ID, "email_create")
    SUBMIT_BUTTON = (By.ID, 'SubmitCreate')
    GENDER = (By.ID, 'id_gender2')
    FIRSTNAME = (By.ID, "customer_firstname")
    LASTNAME = (By.ID, "customer_lastname")
    PASSWORD = (By.ID, "passwd")
    ADDRESS = (By.ID, "address1")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    POSTCODE = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    PHONENUM = (By.ID, "phone_mobile")
    CREATE_BUTTON = (By.ID, 'submitAccount')
    MESSAGE_ERROR = (By.ID, "create_account_error")
    ACCOUNT_NAME = (By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    """This is used to get the page title"""
    """This is used to login to app"""

    def is_create_account_error_exist(self):
        return self.is_visible(self.MESSAGE_ERROR)

    def account_name_after_log_in(self):
        return self.get_element_text(self.ACCOUNT_NAME)

    def get_error_message(self):
        return self.get_element_text(self.MESSAGE_ERROR)

    def click_sign_in(self):
        self.do_click(self.SIGNIN_BUTTON)

    def submit_email(self, email):
        self.do_send_keys(self.EMAIL, email)
        self.do_click(self.SUBMIT_BUTTON)

    def create_account(self,
                       firstname,
                       lastname,
                       password,
                       address,
                       city,
                       state,
                       postcode,
                       country,
                       phonenum):
        self.do_click(self.GENDER)
        self.do_send_keys(self.FIRSTNAME, firstname)
        self.do_send_keys(self.LASTNAME, lastname)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.ADDRESS, address)
        self.do_send_keys(self.CITY, city)
        self.do_select(self.STATE, state)
        self.do_send_keys(self.POSTCODE, postcode)
        self.do_select(self.COUNTRY, country)
        self.do_send_keys(self.PHONENUM, phonenum)
        self.do_click(self.CREATE_BUTTON)
