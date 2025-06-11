import pytest

from pages.Elements.text_box import TextBox

link = "https://demoqa.com/text-box"


class TestTextBox:
    def test_list_collapse(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_lists_can_collapse()

    def test_banner_loaded(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_banner_right()

    def test_text_box_is_all_elements_present(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.is_all_elements_present()

    def test_check_logo(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_logo()

    def test_select_from_list(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.select_from_sidebar('Alerts')

    @pytest.mark.smoke
    def test_submit_form(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        name, email, address, perm_address = text_box.submit_form_valid()  # Вызываем один раз
        text_box.check_success_message(name, email, address, perm_address)

    def test_submit_form_custom_email(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        name, email, address, perm_address = text_box.submit_form_custom("email", "zhopa228@gmail.com")
        text_box.check_success_message(name, email, address, perm_address)

    @pytest.mark.smoke
    def test_submit_form_invalid_email(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.submit_form_custom("email", "zhopa228@@gmail.com")
        text_box.check_field_has_error(text_box.email_input)
        text_box.success_message_doesnt_appear()
