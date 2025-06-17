from pages.Alerts_Frame_Windows.nested_frames_page import NestedFramesPage
import pytest
import allure

link = 'https://demoqa.com/nestedframes'

@allure.parent_suite("Тесты Alerts Frames and Windows")
@allure.suite("Тесты родственных модальных окон")
@pytest.mark.Alerts_Frame_Windows
class TestNestedFramesPage:
    @allure.title("На странице находится родительский iframe с текстом Parent frame")
    def test_parent_frame(self, page):
        frames = NestedFramesPage(page)
        frames.open(link)
        frames.check_parent_frame()
    @allure.title("При клике на Small modal появляется большое модальное окно")
    def test_child_frame(self, page):
        frames = NestedFramesPage(page)
        frames.open(link)
        parent = frames.check_parent_frame()
        frames.check_child_frame(parent)
