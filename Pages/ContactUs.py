from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

"""login - điền email vào newsletter và submit"""


class ContacUs(BasePage):
    """by locator"""
    BUTTON_INFORMATION = (By.XPATH, '/html/body/div/div[3]/footer/div/section[3]/h4')
    BUTTON_CONTACT = (By.XPATH, '/html/body/div/div[3]/footer/div/section[3]/ul/li[5]/a')
    CHOOSE_SUBJECT_HEADING = (By.ID, 'id_contact')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_ORDER_REF = (By.ID, 'id_order')
    ATTACH_FILE = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/p[5]/div')
    INPUT_MESSAGE = (By.ID, 'message')
    BUTTON_SEND = (By.ID, 'submitMessage')
    MESSAGE_SUCCESS = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def input_contact(self,
                      subject,
                      email,
                      order,
                      path,
                      message):
        self.do_click(self.BUTTON_INFORMATION)
        self.do_click(self.BUTTON_CONTACT)
        self.do_select(self.CHOOSE_SUBJECT_HEADING, subject)
        self.do_send_keys(self.INPUT_EMAIL, email)
        self.do_send_keys(self.INPUT_ORDER_REF, order)
        self.do_choose_file(self.ATTACH_FILE, path)
        self.do_send_keys(self.INPUT_MESSAGE, message)
        self.do_click(self.BUTTON_SEND)

    def show_message(self):
        return self.get_element_text(self.MESSAGE_SUCCESS)
