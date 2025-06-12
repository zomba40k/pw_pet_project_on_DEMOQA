import pytest

from pages.Elements.web_table import WebTable

link = 'https://demoqa.com/webtables'


@pytest.mark.Elements
class TestWebTable:

    def test_form_opens(self, page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.check_form_appeared()

    def test_send_form(self, page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.send_reg_form()

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
        page = WebTable(page)
        page.open(link)
        page.add_click()

        page.send_custom_reg_form(email=email, age=age, salary=salary)
        page.check_field_invalid(page.email)
        page.check_field_invalid(page.age)
        page.check_field_invalid(page.salary)

    def test_search_box(self, page):
        page = WebTable(page)
        page.open(link)
        row_data = ["Vega"]

        page.search('Vega')
        page.check_data_added(row_data)

    def test_invalid_search_box(self, page):
        page = WebTable(page)
        page.open(link)
        page.search('Balls')
        page.check_table_is_empty()

    def test_edit_button(self, page):
        page = WebTable(page)
        page.open(link)
        page.edit_row_by_text('Vega')

    def test_delete_button(self, page):
        page = WebTable(page)
        page.open(link)
        page.delete_row_by_text('Vega')
        page.check_data_deleted(row_data=['Vega'])
