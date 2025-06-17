import pytest
import allure
from pages.Elements.upload_and_download_page import UploadAndDownloadPage

link = 'https://demoqa.com/upload-download'

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты загрузки и закачки файлов")
@pytest.mark.Elements
class TestUploadAndDownload:
    @allure.title("По клику на кнопку кнопку 'Download' начинается загрузка файла sampleFile.jpeg")
    def test_upload(self, page):
        upload_page = UploadAndDownloadPage(page)
        upload_page.open(link)
        upload_page.upload()

    @allure.title('По клику на выбрать файл появляется возможность выбрать файл, имя и путь к файлу отображаются')
    def test_download(self, page, tmp_path):
        download_page = UploadAndDownloadPage(page)
        download_page.open(link)
        file_path = download_page.download(target_dir='test_data')

        download_page.is_downloaded(file_path)
        download_page.delete_file(file_path)
