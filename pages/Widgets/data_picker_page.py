from faker import Faker
import datetime
from pages.base_page import BasePage
fake = Faker()

class DataPickerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.date_picker = self.page.locator('#datePickerMonthYearInput')
        self.date_time_picker = self.page.locator('#dateAndTimePickerInput')


    def fill_date(self,locator):

        date = fake.date(pattern='%m/%d/%Y')
        locator.fill(date)
        return date

    def check_date_is_right(self,date,locator):

        field = locator.input_value()
        assert date ==field, 'Date is incorrect'

    def select_date_via_picker(self, day:int, month:int, year:int,time:str,locator):
        """:param day: День (1-31)
        :param month: Месяц (1-12)
        :param year: Год (например 2025)
        :param time: Время в формате 'HH:MM' (например '15:30')
        :return: Возвращает выбранную дату в формате 'June 11, 2025 6:45 PM'
        :param locator: Локатор поля (например page.date_picker)
        """
        locator.click()

        self.page.locator('.react-datepicker__month-select').select_option(value=str(month-1))
        self.page.locator('.react-datepicker__year-select').select_option(value=str(year))
        self.page.locator(f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)").click()
        if locator == self.date_time_picker:
            self.page.locator('li.react-datepicker__time-list-item',has_text=time)
        return f'{month}/{day}/{year}'

