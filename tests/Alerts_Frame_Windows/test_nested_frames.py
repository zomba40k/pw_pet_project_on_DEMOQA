from pages.Alerts_Frame_Windows.nested_frames_page import NestedFramesPage
import pytest

link = 'https://demoqa.com/nestedframes'

@pytest.mark.Alerts_Frame_Windows

class TestNestedFramesPage:

    def test_nested_frame(self, page):
        frames = NestedFramesPage(page)
        frames.open(link)
        parent = frames.check_parent_frame()
        frames.check_child_frame(parent)
