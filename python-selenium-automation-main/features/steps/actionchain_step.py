from behave import given, when, then

@when('Click on "{link}" link')
def click_link(context, link):
    context.actionchain_page.click_link(link)


@when('Hover over the first user avatar')
def hover_first_user_avatar(context):
    context.actionchain_page.hover_first_user_avatar()


@when('Click on View profile link')
def click_view_profile_link(context):
    context.actionchain_page.click_view_profile_link()


@then('Verify "{text}" text is displayed')
def verify_text(context, text):
    context.actionchain_page.verify_page_text(text)