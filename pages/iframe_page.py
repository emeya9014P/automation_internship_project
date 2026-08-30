import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class IFramePage(BasePage):
    FRAME_LINK = (By.XPATH, "//a[text()='Frames']")
    IFRAME_ELEMENT = (By.ID, "mce_0_ifr")
    IFRAME_LINK = (By.XPATH, "//a[text()='iFrame']")
    TEXT_INPUT_BODY = (By.ID, "tinymce")
    CLOSE_BANNER_BUTTON = (By.CSS_SELECTOR, "button[class*='tox-notification__dismiss']")

    def open_webpage_for_iframe(self):
        self.open_url(config.HEROKU_URL)

    def click_on_frames(self):
        self.click_element(self.FRAME_LINK)

    def click_on_iframe(self):
        self.click_element(self.IFRAME_LINK)

    def enter_text_in_iframe(self, text):
        self.driver.switch_to.frame(self.find_element(self.IFRAME_ELEMENT))
        # JS로 기존 문구를 깔끔하게 지우고 새 텍스트를 바로 대입
        self.driver.execute_script(
            "arguments[0].innerText = arguments[1];",
            self.find_element(self.TEXT_INPUT_BODY),
            text,
        )

    def verify_iframe_text(self, expected_text):
        actual_text = self.find_element(self.TEXT_INPUT_BODY).text
        self.driver.switch_to.default_content()  # 검증 완료 후 프레임 복귀
        assert (
                actual_text == expected_text
        ), f"Expected '{expected_text}' but found '{actual_text}'"