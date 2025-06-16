import pytest
import allure
from pages.Elements.broken_links_page import BrokenLinksPage

link = 'https://demoqa.com/broken'

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты сломанных ссылок")
@pytest.mark.Elements
class TestBrokenLinks:
    @allure.title("Изображение под текстом 'Valid image' Загружается корректно")
    def test_valid_image(self, page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.is_image_valid(broken_links.valid_image)

    @allure.title("Изображение под текстом 'Broken image' не загружается")
    def test_broken_image(self, page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.is_image_not_broken(broken_links.broken_image)

    @allure.title("Ссылка под текстом 'Valid Link' рабочая")
    def test_valid_link(self, page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.check_valid_link()

    @allure.title("Ссылка под текстом 'Broken Link' сломана")
    def test_broken_link(self, page):
        broken_links = BrokenLinksPage(page)
        broken_links.open(link)
        broken_links.check_broken_link()
