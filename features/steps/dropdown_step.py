from behave import when, then

@when('Click on Dropdown link')
def click_dropdown_link(context):
    context.dropdown_page.click_dropdown_link()


@when('Select "{option}" from dropdown option')
def select_dropdown_option(context, option):
    context.dropdown_page.select_dropdown_option(option)


@then('Verify selected dropdown option is "{text}"')
def verify_selected_option(context, text):
    context.dropdown_page.verify_selected_option(text)
