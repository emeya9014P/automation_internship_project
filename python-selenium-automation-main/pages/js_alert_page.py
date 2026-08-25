from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JSAlertPage(BasePage):
    CLICK_FOR_JS_ALERT_BUTTON = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    JAVASCRIPT_ALERT_LINK = (By.CSS_SELECTOR, "a[href='/javascript_alerts']")
    RESULT_TEXT = (By.CSS_SELECTOR, "#result")

    def click_javascript_alerts_link(self):
        self.click_element(self.JAVASCRIPT_ALERT_LINK)

    def click_click_for_js_alert_button(self):
        self.click_element(self.CLICK_FOR_JS_ALERT_BUTTON)

    def click_okay_button(self):
        self.accept_alert()

    def verify_result_text_shown(self, expected_text):
        actual_text = self.find_element(self.RESULT_TEXT).text
        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_text}' and found '{actual_text}'")
