from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.product_search_page import ProductSearchPage
from pages.off_plan_page import OffPlanPage


def browser_init(context):
    """
    :param context: Behave context
    """

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")  # 봇 흔적 지우기
    options.add_argument("--incognito")  # 시크릿 모드로 켜서 청정한 상태 유지
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

    context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.product_search_page = ProductSearchPage(context.driver)
    context.off_plan_page = OffPlanPage(context.driver)


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
