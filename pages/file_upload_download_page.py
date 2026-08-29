import os
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FileUploadDownloadPage(BasePage):
    DOWNLOAD_BUTTON = (By.ID, 'downloadButton')
    FILE_INPUT = (By.ID, "uploadFile")

    def open_the_webpage(self):
        self.open_url("https://www.tutorialspoint.com/selenium/practice/upload-download.php")

    def click_download_button(self):
        self.click_element(self.DOWNLOAD_BUTTON)

    def verify_file_downloaded(self, expected_filename="sampleFile.jpeg", timeout=15):
        download_dir = os.path.abspath("./downloads")
        target_name = expected_filename.split('.')[0].lower()

        end_time = time.time() + timeout
        while time.time() < end_time:
            if os.path.exists(download_dir):
                files = os.listdir(download_dir)
                completed_files = [f for f in files if not f.endswith(('.tmp', '.crdownload'))]

                for file_name in completed_files:
                    if target_name in file_name.lower():
                        return True
            time.sleep(0.5)

        return False

    def upload_sample_file(self, filename):
        # 1. 루트 폴더 우선 탐색 후, 없으면 downloads 폴더 탐색
        file_path = os.path.abspath(filename)
        if not os.path.exists(file_path):
            file_path = os.path.abspath(os.path.join("./downloads", filename))

        # 2. 파일 존재 여부 최종 검증
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No file to upload: {file_path}")

        # 3. BasePage의 upload_file 메서드 호출
        self.upload_file(self.FILE_INPUT, file_path)

    def verify_file_uploaded(self, filename):
        # input의 value 속성(예: C:\fakepath\sample.txt)에서 파일명 포함 여부 확인
        uploaded_value = self.find_element(self.FILE_INPUT).get_attribute("value") or ""
        return filename.lower() in uploaded_value.lower()
