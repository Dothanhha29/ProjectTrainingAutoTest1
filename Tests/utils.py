

def get_screenshot(driver):
    driver.save_screenshot("screenshot.png")


def screenshot_decorator(driver):
    def wrap_wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except AssertionError:
                get_screenshot(driver)
                raise
        return wrapper
    return wrap_wrapper
