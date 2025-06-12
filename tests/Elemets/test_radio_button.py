import pytest

from pages.Elements.radio_button import RadioButton

link = 'https://demoqa.com/radio-button'


@pytest.mark.Elements
class TestRadioButton:

    def test_logo(self, page):
        radio = RadioButton(page)
        radio.open(link)
        radio.check_page('radio-button')
        radio.click_logo()

        radio.check_page()

    def test_yes_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.click_radio('yes')
        radiobutton.check_succes_message('Yes')

    def test_impressive_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.click_radio('impressive')
        radiobutton.check_succes_message('Impressive')

    def test_no_button(self, page):
        radiobutton = RadioButton(page)
        radiobutton.open(link)
        radiobutton.check_no()
