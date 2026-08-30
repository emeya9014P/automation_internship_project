from behave import given, when, then
from pages.js_alert_page import JSAlertPage

@given('Go to the-internet.herokuapp.com for jsalert test')
def open_webpage_for_jsalert(context):
    context.js_alert_page = JSAlertPage(context.driver)
    context.js_alert_page.open_webpage_for_jsalert()


@when('Click on JavaScript Alerts link')
def click_javascript_alerts_link(context):
    context.js_alert_page.click_javascript_alerts_link()


@when('Click on "Click for JS Alert" button')
def click_click_for_js_alert_button(context):
    context.js_alert_page.click_click_for_js_alert_button()


@then('Click "Okay" button in the alert window')
def click_okay_button(context):
    context.js_alert_page.click_okay_button()


@then('Verify result "{text}" shown')
def verify_result_text_shown(context, text):
    context.js_alert_page.verify_result_text_shown(text)
