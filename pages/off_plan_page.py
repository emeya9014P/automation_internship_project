from selenium import webdriver
import config
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OffPlanPage(BasePage):

    CONTINUE_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")
    MAIN_FILTER_RESULT = (By.XPATH, "(//button[@data-test-id='search-and-filters-button'])[2]")
    MOBILE_MAIN_FILTER_RESULT = (By.XPATH, "//*[text()='1 Filter is active']")
    OFF_PLAN_MENU = (By.XPATH, "//a[@aria-label='Off-plan' or contains(., 'Off-plan')]")
    OFF_PLAN_MENU_MOBILE = (By.XPATH, "//span[text()='Off-plan']")
    OFF_PLAN_PAGE_PARTIAL_URL = "https://find.reelly.io"
    OUT_OF_STOCK_ICON = (By.CSS_SELECTOR, "div[data-test-id='filter-badge-out_of_stock']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#field")
    MODAL_FILTER_RESULT_BTN = (By.CSS_SELECTOR, "button[data-test-id='all-filters-submit']")
    SEARCH_AND_FILTER_BTN = (By.XPATH, "(//button[@data-test-id='search-and-filters-button'])[2]")
    SEARCH_AND_FILTER_MOBILE_BTN = (By.XPATH, "//button[@data-test-id='search-and-filters-button']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email-2")

    def login_to_page(self):
        # 1. 도메인 쿠키 컨텍스트 형성을 위해 접속
        self.driver.get("https://find.reelly.io/")
        time.sleep(1)

        # 기존 쿠키 제거 (혹시 남은 만료 세션 정리)
        self.driver.delete_all_cookies()

        # 2. 토큰 주입 (Secure 및 domain 옵션 세분화)
        self.driver.add_cookie({
            'name': 'auth_access_token',
            'value': config.AUTH_ACCESS_TOKEN,
            'domain': '.find.reelly.io',  # 필요에 따라 'find.reelly.io' 또는 '.find.reelly.io'
            'path': '/',
            'secure': True
        })
        self.driver.add_cookie({
            'name': 'auth_refresh_token',
            'value': config.AUTH_REFRESH_TOKEN,
            'domain': '.find.reelly.io',
            'path': '/',
            'secure': True
        })

        # 3. 로그인 상태 적용을 위해 대시보드 URL로 직접 이동 또는 refresh
        self.driver.get("https://find.reelly.io/")
        time.sleep(3)

        print(f"Current URL after refresh: {self.driver.current_url}")

    def click_off_plan_menu(self):
        time.sleep(1)

        window_width = self.driver.execute_script("return window.innerWidth;")

        if window_width < 768:
            print("mobile mode")
            self.wait_until_clickable_click(self.OFF_PLAN_MENU_MOBILE)
        else:
            print("PC mode")
            self.wait_until_clickable_click(self.OFF_PLAN_MENU)

    def verify_off_plan_page_opened(self):
        self.wait_until_url_contains(self.OFF_PLAN_PAGE_PARTIAL_URL)

    def click_search_and_filters_btn(self):
        window_width = self.driver.execute_script("return window.innerWidth;")

        if window_width < 768:
            print(f"mobile mode")
            self.wait_until_clickable_click(self.SEARCH_AND_FILTER_MOBILE_BTN)
        else:
            print(f"PC mode")
            self.wait_until_clickable_click(self.SEARCH_AND_FILTER_BTN)

    def click_out_of_stock_btn(self):
        button = self.find_element(self.OUT_OF_STOCK_ICON)
        self.driver.execute_script("arguments[0].click();", button)
        self.wait_until_clickable_click(self.MODAL_FILTER_RESULT_BTN)

    def verify_filter_result(self):
        window_width = self.driver.execute_script("return window.innerWidth;")

        if window_width < 768:
            print(f"mobile mode")
            self.wait_until_appear(self.MOBILE_MAIN_FILTER_RESULT)
        else:
            print(f"PC mode")
            self.wait_until_appear(self.MAIN_FILTER_RESULT)

