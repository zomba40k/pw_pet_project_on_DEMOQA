from pages.Widgets.tool_tips_page import ToolTipsPage
import pytest

link = 'https://demoqa.com/tool-tips'
#@pytest.mark.xfail(reason="Иногда два tooltip одновременно — баг демо-страницы")
@pytest.mark.Widgets
class TestToolTips:

    def test_btn(self,page):
        btn = ToolTipsPage(page)
        btn.open(link)
        btn.hover_over(btn.tip_btn)
        btn.check_tip('Button')

    def test_text_field(self,page):
        field = ToolTipsPage(page)
        field.open(link)
        field.hover_over(field.text_field)
        field.check_tip('text field')

    def test_contrary(self,page):
        contrary = ToolTipsPage(page)
        contrary.open(link)
        contrary.hover_over(contrary.contrary_text)
        contrary.check_tip('Contrary')

    def test_numbers(self,page):
        numbers = ToolTipsPage(page)
        numbers.open(link)
        numbers.hover_over(numbers.numbers_text)
        numbers.check_tip('1.10.32')