from datetime import datetime, time
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import sys
import traceback

web_driver = None
def pytest_exception_interact(report):
    print(f'Test exception:\n{report.longreprtext}')
    filename = f"Screenshots/{report.nodeid.split('::')[-1]}.png"
    print(filename)
    web_driver.save_screenshot(filename)


@pytest.fixture(params=["firefox"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    request.cls.driver.set_window_size(1092, 882)
    request.cls.browser = request.param
    yield
    web_driver.close()
