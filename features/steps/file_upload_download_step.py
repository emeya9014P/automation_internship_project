import os
from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.file_upload_download_page import FileUploadDownloadPage
from time import sleep

@given('Go to the Tutorialspoint site')
def open_the_webpage(context):
    context.file_upload_download_page = FileUploadDownloadPage(context.driver)
    context.file_upload_download_page.open_the_webpage()


@when('Click on Download button')
def click_download_button(context):
    # 다운로드 전 잔여 파일 정리
    download_dir = os.path.abspath("./downloads")
    if os.path.exists(download_dir):
        for file in os.listdir(download_dir):
            file_path = os.path.join(download_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                pass

    context.file_upload_download_page.click_download_button()

@then('Verify downloaded file in the downloads directory')
def verify_file_downloaded(context):
    assert context.file_upload_download_page.verify_file_downloaded(), "File download failed."


@when('Upload file "{filename}"')
def upload_sample_file(context, filename):
    context.file_upload_download_page.upload_sample_file(filename)


@then('Verify "{filename}" file is uploaded')
def verify_file_uploaded(context, filename):
    assert context.file_upload_download_page.verify_file_uploaded(filename), f"File {filename} upload failed."