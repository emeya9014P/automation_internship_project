import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN_LINK = (By.CSS_SELECTOR, "a[href='/dropdown']")
    DROPDOWN_OPTION = (By.ID, "dropdown")

    def open_webpage_for_dropdown(self):
        self.open_url(config.HEROKU_URL)

    def click_dropdown_link(self):
        self.click_element(self.DROPDOWN_LINK)

    def select_dropdown_option(self, option):
        self.select_dropdown_by_text(self.DROPDOWN_OPTION, option)

    def verify_selected_option(self, expected_text):
        self.verify_selected_dropdown_text(self.DROPDOWN_OPTION, expected_text)

