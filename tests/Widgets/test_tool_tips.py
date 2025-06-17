from pages.Widgets.tool_tips_page import ToolTipsPage
import pytest
import allure

link = 'https://demoqa.com/tool-tips'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Подсказок")

@pytest.mark.Widgets
class TestToolTips:

    @allure.title('При наведении курсора  на кнопку Hover me to see, появляется подсказка с текстом You howered over the button')
    def test_btn(self,page):
        btn = ToolTipsPage(page)
        btn.open(link)
        btn.hover_over(btn.tip_btn)
        btn.check_tip('Button')

    @allure.title('При наведении курсора на текстовое поле появляется подсказка с текстом You hovered over the text field')
    def test_text_field(self,page):
        field = ToolTipsPage(page)
        field.open(link)
        field.hover_over(field.text_field)
        field.check_tip('text field')

    @pytest.mark.xfail(reason="Иногда два tooltip одновременно — баг демо-страницы")
    @allure.title('При наведении курсора  на гиперссылку на слове Contrary, появляется подсказка с текстом You hovered over the Contrary')
    def test_contrary(self,page):
        contrary = ToolTipsPage(page)
        contrary.open(link)
        contrary.hover_over(contrary.contrary_text)
        contrary.check_tip('Contrary')

    @allure.title('При наведении курсора на гиперссылку на тексте 1.10.32, появляется подсказка You hovered over the 1.10.32')
    def test_numbers(self,page):
        numbers = ToolTipsPage(page)
        numbers.open(link)
        numbers.hover_over(numbers.numbers_text)
        numbers.check_tip('1.10.32')