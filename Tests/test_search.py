import pytest
from Pages.Search import Search
from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestSearch(BaseTest):
    def test_value_in_placeholder(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.RANDOM_STRING)
        placeholder = self.inputSearch.get_placeholder_text(TestData.ATTRIBUTE_PLACEHOLDER)
        input_value = self.inputSearch.get_placeholder_text(TestData.ATTRIBUTE_VALUE)
        self.inputSearch.clear_value()
        value_after_clear = self.inputSearch.get_placeholder_text(TestData.ATTRIBUTE_VALUE)
        validate = TestData.PLACEHOLDER_SEARCH not in input_value
        assert not value_after_clear
        assert placeholder == TestData.PLACEHOLDER_SEARCH
        assert validate

    def test_recommended_text(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.VALID_SEARCH_VALUE)
        flag = self.inputSearch.check_recommend(TestData.VALID_SEARCH_VALUE)
        return flag

    def test_search_result_num(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.VALID_SEARCH_VALUE)
        self.inputSearch.click_search()
        product_num = self.inputSearch.get_product_num()
        title_list = self.inputSearch.get_title_list_search_result(TestData.ATTRIBUTE_TITLE)
        assert int(product_num) == len(title_list)

    def test_result_title(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.VALID_SEARCH_VALUE)
        self.inputSearch.click_search()
        title_list = self.inputSearch.get_title_list_search_result(TestData.ATTRIBUTE_TITLE)
        validation = True
        for title in title_list:
            if TestData.VALID_SEARCH_VALUE not in title:
                validation = False
        assert validation

    def test_element_with_price(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.VALID_SEARCH_VALUE)
        self.inputSearch.click_search()
        title_list = self.inputSearch.get_title_list_search_result(TestData.ATTRIBUTE_TITLE)
        price_list = self.inputSearch.get_price_list_search_result()
        assert len(title_list) == len(price_list)

    def test_submit_search(self):
        self.inputSearch = Search(self.driver)
        self.inputSearch.input_search(TestData.RANDOM_STRING)
        self.inputSearch.click_search()
        msg_success = self.inputSearch.show_message()
        assert msg_success == TestData.MESSAGE_NOTFOUND
