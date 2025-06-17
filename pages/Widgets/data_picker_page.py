from faker import Faker
import calendar
from pages.base_page import BasePage

fake = Faker()


class DataPickerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.date_picker = self.page.locator('#datePickerMonthYearInput')
        self.date_time_picker = self.page.locator('#dateAndTimePickerInput')

    def fill_date(self, locator):
        date = fake.date(pattern='%m/%d/%Y')
        if locator == self.date_time_picker:
            random_datetime = fake.date_time()
            date = random_datetime.strftime("%B %d, %Y %I:%M %p")
        locator.fill(date)
        return date

    def check_date_is_right(self, date, locator):
        if locator == self.date_picker:
            field = locator.input_value()
            assert date == field, f'Неверная дата, ожидалось {date}, вышло {field}'
        else:
            field = locator.input_value()
            assert date == field, f'Неверная дата, ожидалось {date}, вышло {field}'

    def select_date_via_picker(self,el, day: int, month: int, year: int, time: str= None ):
        """:param day: День (1-31)
        :param month: Месяц (1-12)
        :param year: Год (например 2025)
        :param time: Время в формате 'HH:MM' (например '15:30')
        :param locator: Локатор поля (например page.date_picker)
        :return: Возвращает выбранную дату в формате 'June 11, 2025 6:45 PM'

        """
        el.click()

        if el == self.date_time_picker:
            self.page.locator('.react-datepicker__year-read-view').click()
            self.page.locator('.react-datepicker__year-option',has_text=str(year)).click()


            self.page.locator('.react-datepicker__month-read-view').click()
            self.page.locator('.react-datepicker__month-option',has_text=calendar.month_name[month]).click()

            self.page.locator(f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)").click()
            self.page.locator('.react-datepicker__time-list-item', has_text=time[:4]).click()
            return f'{calendar.month_name[month]} {day}, {year} {time}'
        else:
            self.page.locator('.react-datepicker__month-select').select_option(value=str(month - 1))
            self.page.locator('.react-datepicker__year-select').select_option(value=str(year))
            self.page.locator(f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)").click()

            return f'{month}/{day}/{year}'
