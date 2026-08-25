from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class IFramePage(BasePage):
    FRAME_LINK = (By.XPATH, "//a[text()='Frames']")
    IFRAME_ELEMENT = (By.ID, "mce_0_ifr")
    IFRAME_LINK = (By.XPATH, "//a[text()='iFrame']")
    TEXT_INPUT_BODY = (By.ID, "tinymce")
    CLOSE_BANNER_BUTTON = (By.CSS_SELECTOR, "button[class*='tox-notification__dismiss']")

    def open_the_webpage(self):
        self.open_url("https://the-internet.herokuapp.com/")

    def click_on_frames(self):
        self.click_element(self.FRAME_LINK)

    def click_on_iframe(self):
        self.click_element(self.IFRAME_LINK)

    def enter_text_in_iframe(self, text):
        # 1. 메인 문서 영역에서 알림 팝업 X 버튼이 떠 있다면 클릭해서 닫기
        try:
            close_btn = self.find_element(self.CLOSE_BANNER_BUTTON)
            close_btn.click()
        except:
            # 팝업이 안 떠 있으면 에러 내지 않고 그냥 패스
            pass

        # 2. iFrame 요소를 기다린 후 화면 전환
        iframe_element = self.wait_until_appear(self.IFRAME_ELEMENT)
        self.driver.switch_to.frame(iframe_element)

        # 3. 에디터 입력창(TEXT_INPUT_BODY) 요소 찾기
        editor = self.wait_until_appear(self.TEXT_INPUT_BODY)

        # 4. JavaScript로 에디터 포커스 및 기존 내용 초기화 (알림창 우회)
        self.driver.execute_script("arguments[0].innerHTML = 'Hello iFrame!';", editor)

        # 4. 텍스트 직접 입력
        editor.send_keys(text)

    def verify_iframe_text(self, expected_text):
        actual_text = self.find_element(self.TEXT_INPUT_BODY).text
        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, '{expected_text}' and found '{actual_text}'")

        # BasePage의 verify_text(locator, expected_text) 메서드를 그대로 재사용!
        # super().verify_text(self.EDITOR_INPUT, expected_text)

        # 검증 후 메인 프레임으로 복귀
        self.driver.switch_to.default_content()