from pages.upload_and_download_page import UploadAndDownloadPage
from pathlib import Path

link = 'https://demoqa.com/upload-download'

class TestUploadAndDownload:

    def test_upload(self,page):
        upload_page = UploadAndDownloadPage(page)
        upload_page.open(link)
        upload_page.upload()

    def test_download(self,page,tmp_path):
        download_page = UploadAndDownloadPage(page)
        download_page.open(link)
        file_path = download_page.download(target_dir=tmp_path)

        download_page.is_downloaded(file_path)


