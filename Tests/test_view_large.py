import time
import pytest
from Pages.ViewLarge import ViewLarge
from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestViewLarge(BaseTest):
    def test_click_button_view_large(self):
        self.viewlarge = ViewLarge(self.driver)
        title_before = self.viewlarge.get_title_before_view_large(TestData.PIC_POSITION)
        self.viewlarge.click_button_view_large(TestData.PIC_POSITION)
        time.sleep(25)
        self.viewlarge.switch_to_frame()
        width = self.viewlarge.get_image_width()
        height = self.viewlarge.get_image_height()
        title_after = self.viewlarge.get_title_after_view_large()
        self.viewlarge.switch_to_default()
        assert title_before == title_after
        assert width == TestData.LARGE_PIC_WIDTH
        assert height == TestData.LARGE_PIC_HEIGHT

    def test_click_on_pic(self):
        self.viewlarge = ViewLarge(self.driver)
        title_before = self.viewlarge.get_title_before_view_large(TestData.PIC_POSITION)
        self.viewlarge.click_on_picture(TestData.PIC_POSITION)
        title_after = self.viewlarge.get_title_after_view_large()
        expect_title = title_after + ' - ' + TestData.PAGE_TITLE
        page_title = self.viewlarge.get_page_title(title_after + ' - ' + TestData.PAGE_TITLE)
        assert expect_title == page_title
        assert title_before == title_after

    def test_change_quantity(self):
        self.viewlarge = ViewLarge(self.driver)
        self.viewlarge.click_button_view_large(TestData.PIC_POSITION)
        time.sleep(25)
        self.viewlarge.switch_to_frame()
        self.viewlarge.scroll_on_iframe(TestData.POSITION_IFRAME)
        self.viewlarge.clear_input_quantity()
        self.viewlarge.input_quantity(TestData.NULL_QUANTITY)
        self.viewlarge.click_add_to_cart()
        time.sleep(25)
        self.viewlarge.switch_to_default()
        mess = self.viewlarge.get_error_message()
        assert mess == TestData.MESS_NULL

    def test_add_to_cart(self):
        self.viewlarge = ViewLarge(self.driver)
        self.viewlarge.click_button_view_large(TestData.PIC_POSITION)
        time.sleep(25)
        self.viewlarge.switch_to_frame()
        self.viewlarge.scroll_on_iframe(TestData.POSITION_IFRAME)
        self.viewlarge.click_add_to_cart()
        self.viewlarge.switch_to_default()
        mess = self.viewlarge.get_success_message()
        title_on_popup = self.viewlarge.get_title_on_success_pop_up()
        self.viewlarge.click_button_close_on_popup_success()
        self.viewlarge.open_cart()
        quantity = self.viewlarge.get_quantity_on_cart(TestData.ATTRIBUTE_VALUE)
        title_on_cart = self.viewlarge.get_title_on_cart()
        assert mess == TestData.MESS_ADD_SUCCESS
        assert quantity == TestData.DEFAULT_QUANTITY
        assert title_on_popup == title_on_cart
