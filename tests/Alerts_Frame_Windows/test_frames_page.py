from pages.Alerts_Frame_Windows.frames_page import FramesPage
import pytest


link = 'https://demoqa.com/frames'

@pytest.mark.Alerts_Frame_Windows
class TestFramesPage:

    def test_frame1(self, page):
        frames = FramesPage(page)
        frames.open(link)
        frames.check_frame1()

    def test_frame2(self, page):
        frames = FramesPage(page)
        frames.open(link)
        frames.check_frame2()
