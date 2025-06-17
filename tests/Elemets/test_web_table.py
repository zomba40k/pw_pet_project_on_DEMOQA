import pytest
import allure
from pages.Elements.web_table import WebTable

link = 'https://demoqa.com/webtables'

@allure.parent_suite("Тесты Elements")
@allure.suite("Тесты Web tables")
@pytest.mark.Elements
class TestWebTable:
    @allure.title('По клику на кнопку Add открывается форма ')
    def test_form_opens(self, page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.check_form_appeared()

    @allure.title('При заполнении формы и клике Submit, данные добавляются в таблицу')
    def test_send_form(self, page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.send_reg_form()

    @allure.title('Проверка отображаются ли данные из формы в таблице')
    def test_data_appears_in_table(self, page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.check_form_appeared()
        row_data = page.send_reg_form()  # список данных
        page.check_data_added(row_data)

    @pytest.mark.parametrize(('email', 'age', 'salary'), [
        ('zhora222@@mail.com', 'ababa', 'not_a_number'),
        ('invalid.email@', '@@', '-1000'),
        ('no_at_sign.com', '___', '!!!'),
        ('', '', '')  # Полностью пустые значения
    ])
    def test_submit_invalid_form(self, page, email, age, salary):
        with allure.step("Проверка невалидации формы"):
            allure.dynamic.title(f"Тест тест с данными: email -  '{email} ' age - '{age}' salary - '{salary}')")
        page = WebTable(page)
        page.open(link)
        page.add_click()

        page.send_custom_reg_form(email=email, age=age, salary=salary)
        page.check_field_invalid(page.email)
        page.check_field_invalid(page.age)
        page.check_field_invalid(page.salary)

    @allure.title('При введении данных в поле поиска выводятся все совпадения')
    def test_search_box(self, page):
        page = WebTable(page)
        page.open(link)
        row_data = ["Vega"]

        page.search('Vega')
        page.check_data_added(row_data)

    @allure.title('При поиске несуществующих данных ничего не выводится')
    def test_invalid_search_box(self, page):
        page = WebTable(page)
        page.open(link)
        page.search('Balls')
        page.check_table_is_empty()

    @allure.title('При клике на кнопку "редактировать"(карандаш) появляется форма с возможность изменения данных ')
    def test_edit_button(self, page):
        page = WebTable(page)
        page.open(link)
        page.edit_row_by_text('Vega')

    @allure.title('При клике на кнопку "удалить"(корзина)строка с данными удаляется')
    def test_delete_button(self, page):
        page = WebTable(page)
        page.open(link)
        page.delete_row_by_text('Vega')
        page.check_data_deleted(row_data=['Vega'])
