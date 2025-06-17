from pages.Widgets.data_picker_page import DataPickerPage
import pytest
import allure

link = 'https://demoqa.com/date-picker'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Date Picker")
@pytest.mark.Widgets
class TestDatePickerPage:

    @allure.title('В поле даты можно вписать дату')
    def test_date_via_field(self, page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.fill_date(page.date_picker)
        page.check_date_is_right(date, page.date_picker)

    @allure.title('Нажав на поле появляется date picker в котором можно выбрать дату в ручную')
    def test_date_via_picker(self, page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.select_date_via_picker( page.date_picker,12, 12, 2022)
        page.check_date_is_right(date, page.date_picker)

    @allure.title('В поле даты можно вписать дату и время')
    def test_date_time_via_field(self, page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.fill_date(page.date_time_picker)
        page.check_date_is_right(date, page.date_time_picker)

    @allure.title('Нажав на поле появляется date picker в котором можно выбрать дату и время в ручную')
    def test_date_time_via_picker(self, page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.select_date_via_picker( page.date_time_picker,12, 12, 2022, '12:30 PM',)
        page.check_date_is_right(date, page.date_time_picker)
