from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

"""login - điền email vào newsletter và submit"""


class Newsletter(BasePage):
    """by locator"""
    NEWSLETTER_INPUT = (By.ID, 'newsletter-input')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div/div[3]/footer/div/div[1]/div/form/div/button')
    MESSAGE_SUCCESS = (By.XPATH, '/html/body/div/div[2]/div/p')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def input_email(self, email):
        self.do_send_keys(self.NEWSLETTER_INPUT, email)
        self.do_click(self.SUBMIT_BUTTON)

    def show_message(self):
        return self.get_element_text(self.MESSAGE_SUCCESS)
