from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OffPlanPage(BasePage):

    CONTINUE_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")
    MAIN_FILTER_RESULT = (By.XPATH, "(//button[@data-test-id='search-and-filters-button'])[2]")
    OFF_PLAN_MENU = (By.CSS_SELECTOR, "a[aria-label='Off-plan']")
    OFF_PLAN_PAGE_PARTIAL_URL = "https://find.reelly.io"
    OUT_OF_STOCK_ICON = (By.CSS_SELECTOR, "div[data-test-id='filter-badge-out_of_stock']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#field")
    MODAL_FILTER_RESULT_BTN = (By.CSS_SELECTOR, "button[data-test-id='all-filters-submit']")
    SEARCH_AND_FILTER_BTN = (By.XPATH, "(//button[@data-test-id='search-and-filters-button'])[2]")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email-2")


    def open_testing_page(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def login_to_page(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.CONTINUE_BTN)

    def click_off_plan_menu(self):
        self.wait_until_clickable_click(self.OFF_PLAN_MENU)

    def verify_off_plan_page_opened(self):
        self.wait_until_url_contains(self.OFF_PLAN_PAGE_PARTIAL_URL)

    def click_search_and_filters_btn(self):
        self.wait_until_clickable_click(self.SEARCH_AND_FILTER_BTN)

    def click_out_of_stock_btn(self):
        button = self.find_element(self.OUT_OF_STOCK_ICON)
        self.driver.execute_script("arguments[0].click();", button)
        self.wait_until_clickable_click(self.MODAL_FILTER_RESULT_BTN)

    def verify_filter_result(self):
        self.wait_until_appear(self.MAIN_FILTER_RESULT)

