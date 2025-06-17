import pytest
import allure
from pages.Elements.radio_button import RadioButton

link = 'https://demoqa.com/radio-button'

@allure.parent_suite("Тесты Elements")
@allure.suite("Тесты Радио-кнопок, тесты работы гиперссылки в лого")
@pytest.mark.Elements
class TestRadioButton:

    @allure.title("Тест работы гиперссылки")
    def test_logo(self, page):
        radio = RadioButton(page)
        radio.open(link)
        radio.check_page('radio-button')
        radio.click_logo()
        radio.check_page()

    @allure.title('Тест yes кнопки')
    def test_yes_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.click_radio('yes')
        radiobutton.check_succes_message('Yes')

    @allure.title('Тест impressive кнопки')
    def test_impressive_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.click_radio('impressive')
        radiobutton.check_succes_message('Impressive')

    @allure.title('Тест no кнопки')
    def test_no_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.check_no()
