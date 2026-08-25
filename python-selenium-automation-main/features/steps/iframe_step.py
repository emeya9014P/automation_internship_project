from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Go to the-internet.herokuapp.com')
def open_the_webpage(context):
    context.driver.get("https://the-internet.herokuapp.com/")


@when('Click on the Frames')
def click_on_frames(context):
    context.iframe_page.click_on_frames()


@when('Click on the iFrame')
def click_on_iframe(context):
    context.iframe_page.click_on_iframe()


@then('Enter text "{text}"')
def enter_text_in_iframe(context, text):
    context.iframe_page.enter_text_in_iframe(text)


@then('Verify the text inside iframe "{text}"')
def verify_iframe_text(context, text):
    context.iframe_page.verify_iframe_text(text)



