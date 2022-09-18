import pytest
from Pages.CreateAccount import LoginPage
from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestLogin(BaseTest):
    def test_email_fail(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_sign_in()
        self.loginPage.submit_email(TestData.EMAIL_F)
        error_msg = self.loginPage.get_error_message()
        assert error_msg == TestData.MESS_INVALID_EMAIL

    def test_create_success(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_sign_in()
        email = TestData.random_email(self.browser)
        self.loginPage.submit_email(email)
        self.loginPage.create_account(TestData.CUSTOMER_FIRST_NAME,
                                      TestData.CUSTOMER_LAST_NAME,
                                      TestData.PASSWORD,
                                      TestData.ADDRESS,
                                      TestData.CITY,
                                      TestData.VALUE_STATE,
                                      TestData.POSTCODE,
                                      TestData.ID_COUNTRY,
                                      TestData.PHONE_MOBILE)
        account_name = self.loginPage.account_name_after_log_in()
        assert account_name == TestData.ACCOUNT_NAME
