import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class WindowHandlePage(BasePage):
    CLICK_HERE_LINK = (By.CSS_SELECTOR, "a[href='/windows/new']")
    MULTIPLE_WINDOWS_LINK = (By.CSS_SELECTOR, "a[href='/windows']")
    NEW_WINDOW_TEXT = (By.XPATH, "//h3[text()='New Window']")
    ORIGINAL_WINDOW_HEADER= (By.XPATH, "//*[text()='Opening a new window']")

    def open_webpage_window_handle(self):
        self.open_url(config.HEROKU_URL)

    def click_multiple_windows_link(self):
        self.click_element(self.MULTIPLE_WINDOWS_LINK)

    def click_click_here_link(self):
        self.click_element(self.CLICK_HERE_LINK)

    def verify_new_window_text(self, expected_text):
        actual_text = self.find_element(self.NEW_WINDOW_TEXT).text
        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_text}' and found '{actual_text}'")

    def switch_back_to_original_window(self):
        self.switch_to_original_window(self.original_window)

    def verify_original_window_header(self, expected_text):
        actual_text = self.find_element(self.ORIGINAL_WINDOW_HEADER).text
        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_text}' and found '{actual_text}'")

