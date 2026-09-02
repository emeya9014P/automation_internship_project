import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

# Page Objects Import
from pages.product_search_page import ProductSearchPage
from pages.off_plan_page import OffPlanPage
from pages.iframe_page import IFramePage
from pages.window_handle_page import WindowHandlePage
from pages.js_alert_page import JSAlertPage
from pages.dropdown_page import DropdownPage
from pages.actionchain_page import ActionChainPage
from pages.file_upload_download_page import FileUploadDownloadPage

def browser_init(context):
    """
    :param context: Behave context
    """
    # CI/CD Test Update
    # ⚙️ 테스트 실행 환경 설정 ("chrome", "chrome_mobile", "chrome_headless", "firefox", "firefox_headless")
    if os.getenv('CI'):
        browser_type = "chrome_headless"
    else:
        browser_type = "chrome"

    # 1. 프로젝트 내 downloads 폴더의 절대 경로 생성 및 폴더가 없으면 자동 생성
    download_dir = os.path.abspath("./downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    if browser_type == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--incognito")

        # 💡 Chrome에 다운로드 폴더 경로 및 팝업 차단 prefs 주입!
        prefs = {
            "download.default_directory": download_dir,  # 다운로드 파일이 저장될 프로젝트 폴더 경로
            "download.prompt_for_download": False,  # 다운로드 시 저장 위치 묻는 팝업 안 띄움
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)

        context.driver = webdriver.Chrome(options=options)
        context.driver.maximize_window()

    elif browser_type == "chrome_mobile":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--incognito")

        # 📱 Mobile Emulation 설정
        mobile_emulation = {"deviceName": "Nexus 5"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        context.driver = webdriver.Chrome(options=options)

    elif browser_type == "chrome_headless":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")  # Headless 모드 가상 해상도 고정

        context.driver = webdriver.Chrome(options=options)

    elif browser_type == "firefox":
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()

    elif browser_type == "firefox_headless":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        context.driver = webdriver.Firefox(options=options)

    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    chrome_options = Options()

    # GitHub Actions 환경을 위한 Headless 및 가상 창 크기 설정
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)

    # Page Objects 초기화
    context.product_search_page = ProductSearchPage(context.driver)
    context.off_plan_page = OffPlanPage(context.driver)
    context.iframe_page = IFramePage(context.driver)
    context.window_handle_page = WindowHandlePage(context.driver)
    context.js_alert_page = JSAlertPage(context.driver)
    context.dropdown_page = DropdownPage(context.driver)
    context.actionchain_page = ActionChainPage(context.driver)
    context.file_upload_download_page = FileUploadDownloadPage(context.driver)

def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()


############## BrowserStack Code (PC mode)##############

# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#
# def before_scenario(context, scenario):
#     bstack_options = {
#         "os": "Windows",
#         "osVersion": "11",
#         "browserName": "Chrome", # if testing Firefox, 1. change to Firefox,
#         "browserVersion": "latest",
#         "userName": "ChanUserName", # before pushing replace with "ChanUserName"
#         "accessKey": "ChanAccessKey", # before pushing replace with "ChanAccessKey"
#         "sessionName": scenario.name,
#         "buildName": scenario.feature.name,
#         "projectName": "Internship_Project",
#         "local": "false"
#     }
#
#     options = ChromeOptions() # if testing Firefox, 2. change to FirefoxOptions()
#     # options for avoid robot chatcha
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--incognito")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
#
#     options.set_capability('bstack:options', bstack_options)
#     bs_url = f"https://{bstack_options['userName']}:{bstack_options['accessKey']}@hub-cloud.browserstack.com/wd/hub"
#
#     # 원격 브라우저 실행
#     context.driver = webdriver.Remote(
#         command_executor=bs_url,
#         options=options
#     )
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#
#     context.product_search_page = ProductSearchPage(context.driver)
#     context.off_plan_page = OffPlanPage(context.driver)
#
#     context.wait = WebDriverWait(context.driver, 10)
#
# def after_scenario(context, scenario):
#     context.driver.quit()


############## BrowserStack Code (Mobile Emulation mode)##############

# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#
# def before_scenario(context, scenario):
#     bstack_options = {
#         "browserName": "chrome",          # 안드로이드폰 안에서 켤 브라우저
#         "deviceName": "Google Pixel 8",  # 👈 여기에 원하는 실제 기기명을 적습니다!
#         "osVersion": "14.0",              # 안드로이드 OS 버전
#         "userName": "ChanUserName",    # 👈
#         "accessKey": "ChanAccessKey",  # 👈
#         "sessionName": scenario.name,
#         "buildName": scenario.feature.name,
#         "projectName": "Internship_Project",
#         "local": "false"
#     }
#
#     options = ChromeOptions() # if testing Firefox, 2. change to FirefoxOptions()
#     # ⭕ 기존 로봇 차단 옵션 (robot chatcha)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--incognito")
#     options.add_argument("--disable-notifications")  # 📱 모바일/로컬 알림 차단
#
#     # ➕ 팝업 차단 옵션
#     prefs = {
#         "profile.default_content_setting_values.notifications": 2,  # 알림 차단
#         "profile.default_content_setting_values.geolocation": 2  # 위치 정보 차단
#     }
#     options.add_experimental_option("prefs", prefs)
#
#     options.set_capability('bstack:options', bstack_options)
#     # ② 📱 안드로이드 시스템 팝업 자동 허용 옵션을 '바깥쪽'에 따로 주입!
#     options.set_capability('appium:autoGrantPermissions', True)
#
#     # 3. 원격 서버 연결
#     bs_url = f"https://{bstack_options['userName']}:{bstack_options['accessKey']}@hub-cloud.browserstack.com/wd/hub"
#
#     # 원격 브라우저 실행
#     context.driver = webdriver.Remote(
#         command_executor=bs_url,
#         options=options
#     )
#
#     # context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#
#     context.product_search_page = ProductSearchPage(context.driver)
#     context.off_plan_page = OffPlanPage(context.driver)
#
#     context.wait = WebDriverWait(context.driver, 10)
#
# def after_scenario(context, scenario):
#     context.driver.quit()