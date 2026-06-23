from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions # for browserstack
# from selenium.webdriver.firefox.options import Options as FirefoxOptions # for browserstack
from selenium.webdriver.chrome.options import Options
from pages.product_search_page import ProductSearchPage
from pages.off_plan_page import OffPlanPage


def browser_init(context):
    """
    :param context: Behave context
    """
    browser_type = "chrome" # test browser를 여기서 정함`

    if browser_type == "chrome":
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")  # 봇 흔적 지우기
        options.add_argument("--incognito")  # 시크릿 모드로 켜서 청정한 상태 유지
        # options.add_argument(
        #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36") # 로봇 캡차 우회

    # 📱 Mobile Emulation 옵션!
        mobile_emulation = {"deviceName": "Nexus 5"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    # 🚀 [Chrome Headless Mode] 활성화 및 창 크기 고정
    #     options.add_argument("--headless")
    #     options.add_argument("--window-size=1920,1080")  # 화면을 안 그리는 대신 해상도를 가상으로 고정해 줌
    #
        # when testing in headless mode: below two codes should be commented out.
        context.driver = webdriver.Chrome(options=options)
        context.driver.maximize_window() # when testing in mobile, comment this out

    elif browser_type == "firefox":
        pass

    # 🦊 [Firefox Headless Mode]  설정
    #     from selenium.webdriver.firefox.options import Options as FirefoxOptions
    #
    #     firefox_options = FirefoxOptions()
    #     firefox_options.add_argument("--headless")
    #     firefox_options.add_argument("--width=1920")
    #     firefox_options.add_argument("--height=1080")
    #
    #     context.driver = webdriver.Firefox(options=firefox_options)

    # when testing in headless mode: below code should be commented out.
    #     context.driver.maximize_window()

    context.driver.implicitly_wait(4)

    context.product_search_page = ProductSearchPage(context.driver)
    context.off_plan_page = OffPlanPage(context.driver)
    context.wait = WebDriverWait(context.driver, 10)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
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
