from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ActionChainPage(BasePage):
    HOVERS_LINK = (By.CSS_SELECTOR, "a[href='/hovers']")
    FIRST_USER_AVATAR = (By.CSS_SELECTOR, ".figure:nth-of-type(1)")
    VIEW_PROFILE_LINK = (By.CSS_SELECTOR, ".figure:nth-of-type(1) .figcaption a")
    NOT_FOUND_TEXT = (By.XPATH, "//*[text()='Not Found']")

    def click_link(self, link):
        link_locator = (By.LINK_TEXT, link)
        self.click_element(link_locator)

    def hover_first_user_avatar(self):
        self.hover_over_element(self.FIRST_USER_AVATAR)

        # 2. 이 페이지 특유의 호버 이슈 우회 처리
        element = self.find_element(self.FIRST_USER_AVATAR)
        self.driver.execute_script(
            "var caption = arguments[0].querySelector('.figcaption');"
            "if(caption) { caption.style.display = 'block'; }",
            element
        )

    def click_view_profile_link(self):
        self.click_element(self.VIEW_PROFILE_LINK)

    def verify_page_text(self, expected_text):
        self.verify_text(self.NOT_FOUND_TEXT, expected_text)