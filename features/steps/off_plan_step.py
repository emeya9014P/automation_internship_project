from behave import given, when, then
from pages.off_plan_page import OffPlanPage


@given("Log in to the page")
def login_to_page(context):
    context.off_plan_page.login_to_page()


@given("Click on the 'Off-plan' menu")
def click_off_plan_menu(context):
    context.off_plan_page.click_off_plan_menu()


@then("Verify the right page opens")
def verify_off_plan_page_opened(context):
    context.off_plan_page.verify_off_plan_page_opened()


@when("Click on the 'Search & filters' button")
def click_search_and_filters_btn(context):
    context.off_plan_page.click_search_and_filters_btn()


@when("Filter it to 'Out of Stock'")
def click_out_of_stock_btn(context):
    context.off_plan_page.click_out_of_stock_btn()


@then("Verify that the results show the 'Out of Stock' tag in the result")
def verify_filter_result(context):
    context.off_plan_page.verify_filter_result()

