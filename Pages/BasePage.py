from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pyautogui
from selenium.webdriver.common.keys import Keys

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_list_of_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_element_2(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def do_click_scroll(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click_escape(self):
        WebDriverWait.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def do_choose_file(self, by_locator, path):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        pyautogui.write(path)
        pyautogui.press('enter')

    def get_attribute_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        return element.get_attribute(text)

    def clear_input_value(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    def do_switch_to_frame(self, by_locator):
        self.driver.switch_to.frame(self.driver.find_element(*by_locator))

    def do_switch_to_default(self):
        self.driver.switch_to.default_content()

    def do_scroll_on_iframe(self, position):
        self.driver.execute_script("window.scrollTo" + position)

    def do_select(self, by_locator, text):
        Select(self.driver.find_element(*by_locator)).select_by_value(text)

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
