import os
from pathlib import Path
from playwright.sync_api import expect, Page
from pages.base_page import BasePage


class UploadAndDownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.download_btn = self.page.locator('#downloadButton')
        self.upload_input = self.page.locator('#uploadFile')
        self.uploaded_path = self.page.locator('#uploadedFilePath')

    def upload(self, file: str = 'test_data/testfile.txt'):
        filename = os.path.basename(file)

        self.upload_input.set_input_files(file)

        expect(self.uploaded_path).to_contain_text(filename)

    def download(self, target_dir=None) -> Path:
        # Если путь не передан — используем папку по умолчанию, например test_data в проекте
        if target_dir is None:
            target_dir = Path(__file__).parent.parent / "test_data"
        # Если передали строку — превращаем в Path
        if not isinstance(target_dir, Path):
            target_dir = Path(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        with self.page.expect_download() as download_info:
            self.download_btn.click()
        download = download_info.value
        download_path = target_dir / download.suggested_filename
        download.save_as(download_path)
        return download_path

    def is_downloaded(self, file_path: Path):
        assert file_path.exists(), f"Файл {file_path} не существует"
        assert file_path.stat().st_size > 0, f"Файл {file_path} пустой"
