from behave import given, when, then
from pages.dropdown_page import DropdownPage

@given('Go to the-internet.herokuapp.com for dropdown test')
def open_webpage_for_dropdown(context):
    context.dropdown_page = DropdownPage(context.driver)
    context.dropdown_page.open_webpage_for_dropdown()


@when('Click on Dropdown link')
def click_dropdown_link(context):
    context.dropdown_page.click_dropdown_link()


@when('Select "{option}" from dropdown option')
def select_dropdown_option(context, option):
    context.dropdown_page.select_dropdown_option(option)


@then('Verify selected dropdown option is "{text}"')
def verify_selected_option(context, text):
    context.dropdown_page.verify_selected_option(text)
