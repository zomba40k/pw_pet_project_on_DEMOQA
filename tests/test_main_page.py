import pytest
import allure
from pages.Elements.main_page import MainPage

card_handle_pairs = [
    ('elements', 'elements'),
    ('forms', 'forms'),
    ('alerts', 'alertsWindows'),
    ('widgets', 'widgets'),
    ('interactions', 'interaction'),
    ('books', 'books')
]
link = 'https://demoqa.com/'

@allure.parent_suite("Тесты Main Page")
@allure.suite("Тесты главной страницы")
class TestMainPage:

    @pytest.mark.parametrize('card,handle', card_handle_pairs)
    def test_click_cards(self, page, card, handle):
        with allure.step(f'Проверка открытия страницы после клика по карточке'):
            allure.dynamic.title(f'Проверка открытия страницы {card} после клика по карточке')
        page = MainPage(page)
        page.open(link)
        page.click_cards(card)
        page.check_page(handle)

    @allure.title('Проверка наличия баннера на странице')
    def test_banner_present(self, page):
        page = MainPage(page)
        page.open(link)
        page.is_banner_present()
