import pytest
import allure
from pages.Elements.text_box import TextBox

link = "https://demoqa.com/text-box"

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты Text Box, тесты раскрывающихся списков тренажеров")
@pytest.mark.Elements
class TestTextBox:

    @allure.title('Списки могут раскрываться')
    def test_list_collapse(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_lists_can_collapse()

    @allure.title('Баннер отображается')
    def test_banner_loaded(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_banner_right()

    @allure.title('Лого отображается')
    def test_check_logo(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.check_logo()

    @allure.title('Из списка тренажеров можно выбрать тренажер')
    def test_select_from_list(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.select_from_sidebar('Alerts')

    @allure.title('Тест отправки формы с валидными данными')
    @pytest.mark.smoke
    def test_submit_form(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        name, email, address, perm_address = text_box.submit_form_valid()  # Вызываем один раз
        text_box.check_success_message(name, email, address, perm_address)

    @allure.title('Тест отправки формы с невалидными данными')
    @pytest.mark.smoke
    def test_submit_form_invalid_email(self, page):
        text_box = TextBox(page)
        text_box.open(link)
        text_box.submit_form_custom("email", "zhopa228@@gmail.com")
        text_box.check_field_has_error(text_box.email_input)
        text_box.success_message_doesnt_appear()
