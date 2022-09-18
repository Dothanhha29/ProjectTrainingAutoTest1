import time
import pytest
from Pages.BuyProduct import BuyProduct
from Config.config import TestData
from Tests.utils import screenshot_decorator
import sys


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestBuyProduct(BaseTest):
    def test_buy_success(self):
        buyProduct = BuyProduct(self.driver)
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '1')

        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '2')
        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '3')
        buyProduct.click_button_proceed_checkout()
        buyProduct.click_button_checkout_sum()
        buyProduct.sign_in(TestData.ACCOUNT_EMAIL, TestData.PASSWORD)
        buyProduct.click_button_checkout_address_ship()
        buyProduct.click_button_checkout_address_ship()
        buyProduct.close_warning_popup()
        buyProduct.check_agree_terms()
        buyProduct.click_button_checkout_address_ship()
        buyProduct.pay_by_bank_wire()
        buyProduct.confirm_order()
        message = buyProduct.show_message_success()
        assert message == TestData.MESSAGE_ORDER_SUCCESS

    def test_change_buy_info(self):
        buyProduct = BuyProduct(self.driver)
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '1')
        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '2')
        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '3')
        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '4')
        buyProduct.click_button_continue()
        buyProduct.click_add_to_cart(TestData.ATTRIBUTE_DATA_ID, '5')
        buyProduct.click_button_continue()
        buyProduct.open_cart()
        buyProduct.edit_quantity('3', '3')
        buyProduct.delete_item('2')
        buyProduct.click_button_checkout_sum()
        buyProduct.sign_in(TestData.ACCOUNT_EMAIL, TestData.PASSWORD)
        buyProduct.click_button_checkout_address_ship()
        buyProduct.click_button_checkout_address_ship()
        buyProduct.close_warning_popup()
        buyProduct.check_agree_terms()
        buyProduct.click_button_checkout_address_ship()
        buyProduct.pay_by_bank_wire()
        buyProduct.confirm_order()
        time.sleep(10)
        message = buyProduct.show_message_success()
        assert message == TestData.MESSAGE_ORDER_SUCCESS

    def test_buy_sale_20_product(self):
        buyProduct = BuyProduct(self.driver)
        buyProduct.find_sale_20_product()
        buyProduct.click_button_continue()
        buyProduct.click_button_proceed_checkout()
        buyProduct.click_button_checkout_sum()
        time.sleep(5)
        buyProduct.sign_in(TestData.ACCOUNT_EMAIL, TestData.PASSWORD)
        time.sleep(5)
        buyProduct.click_button_checkout_address_ship()
        buyProduct.check_agree_terms()
        buyProduct.click_button_checkout_address_ship()
        buyProduct.pay_by_bank_wire()
        buyProduct.confirm_order()
        time.sleep(5)
        message = buyProduct.show_message_success()
        assert message == TestData.MESSAGE_ORDER_SUCCESS
