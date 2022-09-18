from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class ViewLarge(BasePage):
    """by locator"""
    ICON_VIEW_LARGE = (By.XPATH, '//i[@class="icon-eye-open"]')
    LARGE_IMAGE = (By.XPATH, '//span[@id="view_full_size"]//img')
    TITLE = (By.XPATH, '//div[@class="right-block"]//a[@class="product-name"]')
    TITLE_VIEW_LARGE = (By.XPATH, '//div[contains(@class, "pb-center-column")]//h1')
    INPUT_QUANTITY = (By.XPATH, '//*[@id="quantity_wanted"]')
    BUTTON_ADD_TO_CART = (By.XPATH, '//p[@id="add_to_cart"]//button//span')
    ERROR_FANCYBOX = (By.XPATH, '/html/body/div[2]/div/div/div/p')
    MESS_SUCCESS = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/h2')
    TITLE_POP_UP_SUCCESS = (By.XPATH, '//*[@id="layer_cart_product_title"]')
    BUTTON_CLOSE_POP_UP_SUCCESS = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span')
    BUTTON_OPEN_CART = (By.XPATH, '//a[@title="View my shopping cart"]')
    QUANTITY_BOX = (By.XPATH, '//input[@type="text" and contains(@name, "quantity")]')
    TITLE_ON_CART = (By.XPATH, '//td//p[@class="product-name"]//a')
    IFRAME = (By.CLASS_NAME, "fancybox-iframe")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def switch_window(self):
        window = self.driver.window_handles[0]
        self.driver.switch_to_window(window)

    def get_image_width(self):
        return self.get_attribute_text(self.LARGE_IMAGE, "width")

    def get_image_height(self):
        return self.get_attribute_text(self.LARGE_IMAGE, "height")

    def get_title_before_view_large(self, value):
        product_container_path = (
            By.XPATH, '(//ul[@id="homefeatured"]//div[@class="product-container"])[' + value + ']')
        product_container = self.get_element(product_container_path)
        title = product_container.find_element(*self.TITLE)
        return title.text

    def click_button_view_large(self, value):
        product_container_path = (
            By.XPATH, '(//ul[@id="homefeatured"]//div[@class="product-container"])[' + value + ']')
        product_container = self.get_element(product_container_path)
        icon = product_container.find_element(*self.ICON_VIEW_LARGE)
        self.click_scroll(icon)

    def switch_to_frame(self):
        self.do_switch_to_frame(self.IFRAME)

    def switch_to_default(self):
        self.do_switch_to_default()

    def scroll_on_iframe(self, position):
        self.do_scroll_on_iframe(position)

    def get_title_after_view_large(self):
        return self.get_element_text(self.TITLE_VIEW_LARGE)

    def click_on_picture(self, value):
        xpath = '(//ul[@id="homefeatured"]//div[@class="product-container"]//a[@class="product_img_link"])[' + value + ']'
        image_clickable = (By.XPATH, xpath)
        self.do_click_scroll(image_clickable)

    def get_page_title(self, title):
        return self.get_title(title)

    def clear_input_quantity(self):
        self.clear_input_value(self.INPUT_QUANTITY)

    def input_quantity(self, quantity):
        self.do_send_keys(self.INPUT_QUANTITY, quantity)

    def click_add_to_cart(self):
        self.do_click_scroll(self.BUTTON_ADD_TO_CART)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_FANCYBOX)

    def get_success_message(self):
        return self.get_element_text(self.MESS_SUCCESS)

    def get_title_on_success_pop_up(self):
        return self.get_element_text(self.TITLE_POP_UP_SUCCESS)

    def click_button_close_on_popup_success(self):
        self.do_click(self.BUTTON_CLOSE_POP_UP_SUCCESS)

    def open_cart(self):
        self.do_click(self.BUTTON_OPEN_CART)

    def get_quantity_on_cart(self, attribute_value):
        return self.get_attribute_text(self.QUANTITY_BOX, attribute_value)

    def get_title_on_cart(self):
        return self.get_element_text(self.TITLE_ON_CART)
