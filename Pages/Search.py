from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class Search(BasePage):
    """by locator"""
    INPUT_SEARCH = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]')
    BUTTON_SEARCH = (By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button')
    MESSAGE_NOTFOUND = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/p')
    PRODUCT_NUM = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/h1/span[2]')
    AUTOCOMPLETE_SEARCH = (By.CLASS_NAME, 'ac_results')
    TITLE = (By.CLASS_NAME, 'product-name')
    PRICE = (By.CLASS_NAME, 'content_price')
    REDUCTION = (By.CLASS_NAME, 'price-percent-reduction')
    PRODUCT_GRID = (By.CLASS_NAME, 'product_list')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_title_list_search_result(self, attribute_title):
        grid_product = self.get_element(self.PRODUCT_GRID)
        list_product = grid_product.find_elements(*self.TITLE)
        list_title = []
        for element in list_product:
            if element.get_attribute(attribute_title) == '':
                continue
            list_title.append(element.get_attribute(attribute_title))
        return list_title

    def get_price_list_search_result(self):
        list_product = self.get_list_of_element(self.PRICE)
        product_price = []
        for element in list_product:
            if element.find_element(By.CLASS_NAME, "price").text == '':
                continue
            product_price.append(element.find_element(By.CLASS_NAME, "price").text)
        return product_price

    def get_product_num(self):
        quantity = self.get_element_text(self.PRODUCT_NUM).split(" ")
        return quantity[0]

    def check_recommend(self, search_text):
        recommend_list = self.get_element_text(self.AUTOCOMPLETE_SEARCH).split("\n")
        print(recommend_list)
        validation = True
        for item in recommend_list:
            if search_text not in item:
                validation = False
        return validation

    def get_placeholder_text(self, attribute_value):
        return self.get_attribute_text(self.INPUT_SEARCH, attribute_value)

    def clear_value(self):
        self.clear_input_value(self.INPUT_SEARCH)

    def input_search(self, search):
        self.do_send_keys(self.INPUT_SEARCH, search)

    def click_search(self):
        self.do_click(self.BUTTON_SEARCH)

    def show_message(self):
        return self.get_element_text(self.MESSAGE_NOTFOUND)
