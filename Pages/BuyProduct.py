from selenium.common import NoSuchElementException

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

"""login - điền email vào newsletter và submit"""


class BuyProduct(BasePage):
    """by locator order"""
    PAGE = (By.ID, 'homefeatured')
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, 'ajax_add_to_cart_button')
    BUTTON_CONTINUE = (By.XPATH, "//span//span[contains(.,'Continue shopping')]")
    BUTTON_CHECKOUT = (By.XPATH, "//a[contains(@title,'Proceed to checkout')]")
    BUTTON_CHECKOUT_SUM = (By.XPATH, "//p//a[contains(.,'Proceed to checkout')]")
    BUTTON_CHECKOUT_ADDRESS = (By.XPATH, "//button[contains(.,'Proceed to checkout')]")
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    BUTTON_SIGN_IN = (By.ID, 'SubmitLogin')
    BUTTON_CLOSE = (By.XPATH, '//a[@title="Close"]')
    CHECKBOX_AGREE = (By.ID, 'uniform-cgv')
    BUTTON_PAY = (By.XPATH, "//a[@title='Pay by bank wire']")
    BUTTON_CONFIRM = (By.XPATH, '//button[contains(.,"I confirm my order")]')
    BUTTON_OPEN_CART = (By.XPATH, '//a[@title="View my shopping cart"]')
    TEXT_MESSAGE_SUCCESS = (By.CLASS_NAME, "cheque-indent")
    ITEM_BLOCK = (By.XPATH, '//ul[@id="homefeatured"]//div[@class="product-container"]//div[@class="right-block"]')
    SALE_ITEM = (By.CLASS_NAME, 'price-percent-reduction')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_add_to_cart(self, attribute_data_id, text):
        page = self.get_element(self.PAGE)
        buttons = page.find_elements(*self.BUTTON_ADD_TO_CART)
        for button in buttons:
            if button.get_attribute(attribute_data_id) == text:
                self.click_scroll(button)

    def click_button_continue(self):
        self.do_click_scroll(self.BUTTON_CONTINUE)

    def find_sale_20_product(self):
        list_product = self.get_list_of_element(self.ITEM_BLOCK)
        for product in list_product:
            try:
                product.find_element(*self.SALE_ITEM)
            except NoSuchElementException:
                continue
            sale = product.find_element(*self.SALE_ITEM).text
            if sale == "-20%":
                sale_item = product.find_element(*self.BUTTON_ADD_TO_CART)
                sale_item.click()
                break

    def open_cart(self):
        self.do_click_scroll(self.BUTTON_OPEN_CART)

    def edit_quantity(self, value, text):
        textbox_quantity = (By.XPATH, '(//input[@type="text" and contains(@name, "quantity")])[' + value + ']')
        self.clear_input_value(textbox_quantity)
        self.do_send_keys(textbox_quantity, text)

    def delete_item(self, value):
        delete = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr[' + value + ']/td[7]/div/a/i')
        self.do_click_scroll(delete)

    def click_button_proceed_checkout(self):
        self.do_click_scroll(self.BUTTON_CHECKOUT)

    def click_button_checkout_sum(self):
        self.do_click_scroll(self.BUTTON_CHECKOUT_SUM)

    def click_button_checkout_address_ship(self):
        self.do_click(self.BUTTON_CHECKOUT_ADDRESS)

    def sign_in(self, email, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click_scroll(self.BUTTON_SIGN_IN)

    def close_warning_popup(self):
        self.do_click(self.BUTTON_CLOSE)

    def check_agree_terms(self):
        self.do_click(self.CHECKBOX_AGREE)

    def pay_by_bank_wire(self):
        self.do_click(self.BUTTON_PAY)

    def confirm_order(self):
        self.do_click_scroll(self.BUTTON_CONFIRM)

    def show_message_success(self):
        return self.get_element_text(self.TEXT_MESSAGE_SUCCESS)
