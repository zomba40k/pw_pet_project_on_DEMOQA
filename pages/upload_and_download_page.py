from pages.base_page import BasePage
from playwright.sync_api import expect, Page
import os
from pathlib import Path

class UploadAndDownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.download_btn = self.page.locator('#downloadButton')
        self.upload_input = self.page.locator('#uploadFile')
        self.uploaded_path = self.page.locator('#uploadedFilePath')


    def upload(self,file:str='test_data/testfile.txt'):
        filename = os.path.basename(file)

        self.upload_input.set_input_files(file)

        expect(self.uploaded_path).to_contain_text(filename)

    def download(self, target_dir: Path) -> Path:
        with self.page.expect_download() as download_info:
            self.download_btn.click()
        download = download_info.value
        download_path = target_dir / download.suggested_filename
        download.save_as(download_path)
        return download_path

    def is_downloaded(self,file_path:Path):
        assert file_path.exists(), f"Файл {file_path} не существует"
        assert file_path.stat().st_size > 0, f"Файл {file_path} пустой"
