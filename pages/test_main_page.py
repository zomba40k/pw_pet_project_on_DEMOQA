from pages.main_page import MainPage
from pages.check_box import CheckBox
import pytest

card_handle_pairs = [
    ('elements', 'elements'),
    ('forms', 'forms'),
    ('alerts', 'alertsWindows'),
    ('widgets', 'widgets'),
    ('interactions', 'interaction')
]
link = 'https://demoqa.com/'
class TestMainPage:

    @pytest.mark.parametrize('card,handle',card_handle_pairs)
    def test_click_cards(self,page,card, handle):
        page = MainPage(page)
        page.open(link)
        page.click_cards(card)
        page.check_page(handle)


    def test_banner_present(self,page):
        page = MainPage(page)
        page.open(link)
        page.is_banner_present()
