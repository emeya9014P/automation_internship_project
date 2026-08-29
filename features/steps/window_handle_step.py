from behave import when, then

@when ('Click on Multiple Windows link')
def click_multiple_windows_link(context):
    context.window_handle_page.click_multiple_windows_link()


@when ('Click on Click Here link to open new window')
def click_click_here_link(context):
    context.window_handle_page.click_click_here_link()
    # ⚠️ 여기서 새 창으로 스위치를 꼭 호출!
    context.window_handle_page.switch_to_new_window()


@then ('Verify text "{text}" opened in the new window')
def verify_new_window_text(context, text):
    context.window_handle_page.verify_new_window_text(text)


@then('Switch back to original window')
def switch_back_to_original_window(context):
    context.window_handle_page.switch_back_to_original_window()


@then('Verify original window header "{text}" is displayed')
def verify_original_window_header(context, text):
    context.window_handle_page.verify_original_window_header(text)