from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ProductSearchPage(BasePage):

    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_SUBMIT = (By.NAME, 'btnK')
    PARTIAL_URL = "https://www.google.com/search?q=Car"

    def open_google_page(self):
        self.open_url("https://www.google.com/")

    def search_for_product(self, search_word):
        self.input_text(self.SEARCH_INPUT, search_word)

    def click_search_icon(self):
        # self.wait_until_clickable_click(self.SEARCH_SUBMIT)
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)

    def verify_text_result(self, search_word):
        self.verify_url_contains_search_word(search_word)
        # self.wait_until_url_contains(self.PARTIAL_URL)



