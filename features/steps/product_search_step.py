from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.product_search_page import ProductSearchPage
from time import sleep


@given('Open Google page')
def open_google_page(context):
    context.product_search_page = ProductSearchPage(context.driver)
    context.product_search_page.open_google_page()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.product_search_page.search_for_product(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.product_search_page.click_search_icon()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.product_search_page.verify_text_result(search_word)
    # assert search_word.lower() in context.driver.current_url.lower(), \
    #     f'Expected query not in {context.driver.current_url.lower()}'
