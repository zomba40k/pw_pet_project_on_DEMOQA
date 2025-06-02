from pages.base_page import BasePage
from pages.check_box import CheckBox
import pytest

class TestCheckBox():

    @pytest.mark.check_box
    def test_select_desktop_checkbox(self,page):
        checkbox = CheckBox(page)
        checkbox.open()
        checkbox.expand_all()
        checkbox.select_checkbox("Desktop")
        checkbox.check_selected_result("desktop")
