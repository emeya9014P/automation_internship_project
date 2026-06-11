from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url=""):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_until_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        )

    def wait_until_clickable_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        ).click()

    def wait_until_appear(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} not visible"
        )

    def wait_until_url_contains(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f"Expected '{expected_partial_url}' but not in '{self.driver.current_url}'"
        )

    def wait_until_url_to_be(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f"Expected '{expected_url}' but not in '{self.driver.current_url}'"
        )

    def wait_until_visible(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} not visible"
        )

    def verify_url_contains_search_word(self, search_word):
        # 쏙 배달받은 검색어가 주소창에 들어있는지 칼같이 감시하는 공식! 대소문자는 구분 못 함
        self.wait.until(
            EC.url_contains(search_word),
            message=f"Expected '{search_word}' not found in URL"
        )

    def verify_text(self, locator, expected_text):
        actual_text = self.find_element(locator).text
        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_text}' and found '{actual_text}'")

    def verify_partial_text(self, locator, expected_partial_text):
        actual_text = self.find_element(locator).text
        assert expected_partial_text in actual_text, f"Test failed, expected '{expected_partial_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_partial_text}' and found '{actual_text}'")






