import pytest
from Pages.Newsletter import Newsletter
from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestNewsletter(BaseTest):
    def test_submit_newsletter(self):
        self.inputNewsletter = Newsletter(self.driver)
        self.inputNewsletter.input_email(TestData.random_email(self.browser))
        msg_success = self.inputNewsletter.show_message()
        assert msg_success == TestData.MESSAGE_REGISTER_NEWSLETTER_SUCCESS
