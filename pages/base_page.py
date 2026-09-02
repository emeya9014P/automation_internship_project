from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.original_window = None

    def open_url(self, url=""):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click() # 여기서 클릭하니까 페이지 파일 코드에 넣으면 안 됨

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # Multiple Windows Handle
    def switch_to_new_window(self):
        # 1. 스위치하기 '직전'에 현재(원래) 창 핸들을 자동으로 보관!
        self.original_window = self.driver.current_window_handle

        # 2. 새 창으로 스위치
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_original_window(self, *args):
        self.driver.close()  # 새 탭 닫기
        self.driver.switch_to.window(
            self.driver.window_handles[0])

    # Alert
    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()

    # Dropdown
    def select_dropdown_by_text(self, locator, text):
        dropdown_element = self.find_element(locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def verify_selected_dropdown_text(self, locator, expected_text):
        dropdown_element = self.find_element(locator)
        select = Select(dropdown_element)
        actual_text = select.first_selected_option.text.strip()
        expected_text = expected_text.strip()

        assert actual_text == expected_text, f"Test failed, expected '{expected_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_text}' and found '{actual_text}'")

    # ActionChains
    def hover_over_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_until_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        )

    def wait_until_clickable_click(self, locator):
        # 애니메이션 간섭을 우회하기 위해 presence 또는 visibility 대기 후 바로 JS 클릭 실행
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Element by {locator} not found in DOM"
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until_appear(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} not visible"
        )

    def wait_for_disappear(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

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

    def verify_url_contains_search_word(self, search_word):
        # 쏙 배달받은 검색어가 주소창에 들어있는지 칼같이 감시하는 공식! 대소문자는 구분 못 함
        self.wait.until(
            EC.url_contains(search_word),
            message=f"Expected '{search_word}' not found in URL"
        )

    def verify_text(self, locator, expected_text):
        element = self.find_element(locator)
        actual_text = element.text.strip()
        assert actual_text == expected_text.strip(), f"Expected {expected_text}, got {actual_text}"

    def verify_partial_text(self, locator, expected_partial_text):
        actual_text = self.find_element(locator).text
        assert expected_partial_text in actual_text, f"Test failed, expected '{expected_partial_text}' but found '{actual_text}'"
        print(f"Test passed, expected '{expected_partial_text}' and found '{actual_text}'")

    # Upload File
    def upload_file(self, locator, file_path):
        # input[type='file'] 요소를 찾아 절대경로 전달
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(file_path)


