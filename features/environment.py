from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions # for browserstack
from selenium.webdriver.chrome.options import Options
from pages.product_search_page import ProductSearchPage
from pages.off_plan_page import OffPlanPage


# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#
#     browser_type = "chrome" # test browser를 여기서 정함`
#
#     if browser_type == "chrome":
#         options = Options()
#         options.add_argument("--disable-blink-features=AutomationControlled")  # 봇 흔적 지우기
#         options.add_argument("--incognito")  # 시크릿 모드로 켜서 청정한 상태 유지
#         options.add_argument(
#             "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
#
#     # 🚀 [Chrome Headless Mode] 활성화 및 창 크기 고정
#     #     options.add_argument("--headless")
#     #     options.add_argument("--window-size=1920,1080")  # 화면을 안 그리는 대신 해상도를 가상으로 고정해 줌
#     #
#     #     context.driver = webdriver.Chrome(options=options)
#
#         # when testing in headless mode: below code should be commented out.
#         # context.driver.maximize_window()
#
#     elif browser_type == "firefox":
#
#     # 🦊 [Firefox Headless Mode]  설정
#     #     from selenium.webdriver.firefox.options import Options as FirefoxOptions
#     #
#     #     firefox_options = FirefoxOptions()
#     #     firefox_options.add_argument("--headless")
#     #     firefox_options.add_argument("--width=1920")
#     #     firefox_options.add_argument("--height=1080")
#     #
#     #     context.driver = webdriver.Firefox(options=firefox_options)
#
#     # when testing in headless mode: below should be commented out.
#         context.driver.maximize_window()
#
#     context.driver.implicitly_wait(4)
#
#     context.product_search_page = ProductSearchPage(context.driver)
#     context.off_plan_page = OffPlanPage(context.driver)
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, feature):
#     context.driver.quit()


############## BrowserStack Code ##############

def browser_init(context):
    """
    :param context: Behave context
    """

def before_scenario(context, scenario):
    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "userName": "chanpark_FpeZER", # before pushing replace with "ChanUserName"
        "accessKey": "f2RfTyUssGYwyQpshsbD", # before pushing replace with "ChanAccessKey"
        "sessionName": scenario.name,
        "buildName": scenario.feature.name,
        "projectName": "Internship_Project",
        "local": "false"
    }

    options = ChromeOptions()
    # options for avoid robot chatcha
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

    options.set_capability('bstack:options', bstack_options)
    bs_url = f"https://{bstack_options['userName']}:{bstack_options['accessKey']}@hub-cloud.browserstack.com/wd/hub"

    # 원격 브라우저 실행
    context.driver = webdriver.Remote(
        command_executor=bs_url,
        options=options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.product_search_page = ProductSearchPage(context.driver)
    context.off_plan_page = OffPlanPage(context.driver)

    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context, scenario):
    context.driver.quit()
