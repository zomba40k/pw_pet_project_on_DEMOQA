import allure

from pages.Alerts_Frame_Windows.frames_page import FramesPage
import pytest


link = 'https://demoqa.com/frames'

@allure.parent_suite("Тесты Alerts Frames and Windows")
@allure.suite("Тесты фреймов")
@pytest.mark.Alerts_Frame_Windows
class TestFramesPage:

    def test_frame1(self, page):
        frames = FramesPage(page)
        frames.open(link)
        frames.check_frame1()
    @allure.title("В родительсокм iframe находится iframe с текстом Child Iframe")
    def test_frame2(self, page):
        frames = FramesPage(page)
        frames.open(link)
        frames.check_frame2()
