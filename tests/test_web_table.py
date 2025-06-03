from pages.radio_button import RadioButton
import pytest
from pages.web_table import WebTable
import pytest
link = 'https://demoqa.com/webtables'

class TestWebTable:

    def test_form_opens(self,page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.check_form_appeared()

    def test_send_form(self,page):

        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.send_reg_form()

    def test_data_appears_in_table(self,page):
        page = WebTable(page)
        page.open(link)
        page.add_click()
        row_data = page.send_reg_form()  # список данных
        page.check_data_added(row_data)

    @pytest.mark.parametrize(('email', 'age', 'salary'), [
        ('zhora222@@mail.com', 'ababa', 'not_a_number'),
        ('invalid.email@', '@@', '-1000'),
        ('no_at_sign.com', '___', '!!!'),
        ('', '', '')  # Полностью пустые значения
    ])
    def test_submit_invalid_form(self,page,email,age,salary):

        page = WebTable(page)
        page.open(link)
        page.add_click()
        page.send_custom_reg_form(email=email,age=age,salary=salary)
        page.check_field_invalid(page.email)
        page.check_field_invalid(page.age)
        page.check_field_invalid(page.salary)







