import random
import string


class TestData:
    PAGE_TITLE = "My Store"
    PAGE_ACCOUNT_TITLE = "My account - My Store"
    BASE_URL = "https://automationpractice.com/"
    RANDOM_STRING = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    EMAIL = "test" + RANDOM_STRING + "@gmail.com"
    EMAIL_F = "testabc"
    CUSTOMER_FIRST_NAME = "Angela"
    CUSTOMER_LAST_NAME = "Testabc"
    PASSWORD = "Test@12345"
    ADDRESS = "15, 72 lane, ABC street, XYZ district, Hanoi"
    CITY = "Hanoi"
    VALUE_STATE = "2"
    POSTCODE = "12345"
    ID_COUNTRY = "21"
    PHONE_MOBILE = "0912351258"
    ACCOUNT_NAME = "Angela Testabc"
    MESS_INVALID_EMAIL = "Invalid email address."
    MESSAGE_REGISTER_NEWSLETTER_SUCCESS = "Newsletter : You have successfully subscribed to this newsletter."
    CHOOSE_SUBJECT = "2"
    ORDER_REFERENCE = "23435345"
    FILE_PATH = "New Text Document.txt"
    INPUT_MESSAGE = "This is a message"
    MESSAGE_NOTFOUND = 'No results were found for your search "' + RANDOM_STRING + '"'
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_PLACEHOLDER = "placeholder"
    ATTRIBUTE_VALUE = "value"
    ATTRIBUTE_ITEMPRICE = "itemprop"
    ATTRIBUTE_DATA_ID = 'data-id-product'
    PLACEHOLDER_SEARCH = 'Search'
    VALID_SEARCH_VALUE = 'dress'.capitalize()
    ACCOUNT_EMAIL = '9@yopmail.com'
    MESSAGE_ORDER_SUCCESS = "Your order on My Store is complete."
    LARGE_PIC_WIDTH = "458"
    LARGE_PIC_HEIGHT = "458"
    POSITION_IFRAME = "(0, 1096)"
    PIC_POSITION = "1"
    NULL_QUANTITY = "0"
    MESS_NULL = "Null quantity."
    MESS_ADD_SUCCESS = 'Product successfully added to your shopping cart'
    DEFAULT_QUANTITY = "1"
    # def random_email(self, browser):
    #     RANDOM_STRING = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    #     return "test_" + browser + '_' + RANDOM_STRING + "@gmail.com"

    @staticmethod
    def random_email(browser):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        return "test_" + browser + '_' + random_string + "@gmail.com"
