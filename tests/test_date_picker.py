from pages.Widgets.data_picker_page import DataPickerPage
import datetime

link = 'https://demoqa.com/date-picker'


class TestDatePickerPage:


    def test_date_via_field(self,page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.fill_date(page.date_picker)
        page.check_date_is_right(date,page.date_picker)

    def test_date_via_picker(self,page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.select_date_via_picker(12,12,2022,'19:30',locator=page.date_picker)
        page.check_date_is_right(date,page.date_picker)

    def test_date_time_via_field(self,page):
        page = DataPickerPage(page)
        page.open(link)
        date = page.fill_date(page.date_time_picker)
        page.check_date_is_right(date,page.date_time_picker)
        page.page.wait_for_timeout(1000)