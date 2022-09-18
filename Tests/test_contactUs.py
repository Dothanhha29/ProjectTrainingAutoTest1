import pytest
from Pages.ContactUs import ContacUs
from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestContactUs(BaseTest):
    def test_submit_contactus(self):
        self.inputContact = ContacUs(self.driver)
        self.inputContact.input_contact(TestData.CHOOSE_SUBJECT,
                                        TestData.EMAIL,
                                        TestData.ORDER_REFERENCE,
                                        TestData.FILE_PATH,
                                        TestData.INPUT_MESSAGE)
        self.inputContact.show_message()
