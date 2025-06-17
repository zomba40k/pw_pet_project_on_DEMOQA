import allure

from pages.Alerts_Frame_Windows.modals_page import ModalsPage
import pytest

link = 'https://demoqa.com/modal-dialogs'

@allure.parent_suite("Тесты Alerts Frames and Windows")
@allure.suite("Тесты модальных окон")
@pytest.mark.Alerts_Frame_Windows
class TestModals:
    @allure.title("При клике на Small modal появляется маленькое модальное окно")
    def test_small_modals(self, page):
        modals = ModalsPage(page)
        modals.open(link)
        modals.check_small_modal()
    @allure.title("При клике на Small modal появляется большое модальное окно")
    def test_large_modals(self, page):
        modals = ModalsPage(page)
        modals.open(link)
        modals.check_large_modal()
