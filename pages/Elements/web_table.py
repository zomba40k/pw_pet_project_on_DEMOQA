import random

from faker import Faker
from playwright.sync_api import Page, expect

from pages.Elements.base_page import BasePage


def dept_generator():
    while True:
        job = Faker().job()
        if len(job) <= 25:
            return job


class WebTable(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = page.locator('#addNewRecordButton')
        self.first_name = page.get_by_placeholder('First Name')
        self.last_name = page.get_by_placeholder('Last Name')
        self.email = page.get_by_placeholder('name@example.com')
        self.age = page.get_by_placeholder('Age')
        self.salary = page.get_by_placeholder('Salary')
        self.department = page.get_by_placeholder('Department')
        self.submit_button = page.locator('#submit')
        self.search_box = page.locator('#searchBox')
        self.reg_form = page.locator('.modal-content')
        self.empty_table_message = page.locator('.rt-noData')
        self.edit = page.locator('#edit-record-1')
        self.delete = page.locator('#delete-record-1')

    def add_click(self):
        self.add_button.click()

    def check_form_appeared(self):
        expect(self.reg_form).to_be_visible()

    def check_data_added(self, row_data: list[str]):
        rows = self.page.locator(".rt-tr-group")
        count = rows.count()

        for value in row_data:
            found = False
            for i in range(count):
                text = rows.nth(i).inner_text()
                if value in text:
                    found = True
                    break
            assert found, f"Значение '{value}' не найдено ни в одной строке таблицы"

    def send_reg_form(self):
        expect(self.reg_form).to_be_visible()
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        age = str(random.randint(20, 40))
        salary = str(random.randint(100, 800))
        department = dept_generator()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.age.fill(age)
        self.salary.fill(salary)
        self.department.fill(department)

        self.submit_button.click()

        return first_name, last_name, email, age, salary, department

    def send_custom_reg_form(self, **overrides):
        fake = Faker()
        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "age": str(random.randint(20, 40)),
            "salary": str(random.randint(100, 800)),
            "department": fake.job(),

        }
        # Переопределяем значениями из параметров
        data.update(overrides)

        self.first_name.fill(data['first_name'])
        self.last_name.fill(data['last_name'])
        self.email.fill(data['email'])
        self.age.fill(data['age'])
        self.salary.fill(data['salary'])
        self.department.fill(data['department'])
        self.submit_button.click()

    def check_field_invalid(self, locator):
        is_valid = locator.evaluate("el => el.checkValidity()")
        assert not is_valid, "Ожидалось, что поле будет невалидно"

    def check_table_is_empty(self):
        expect(self.empty_table_message).to_be_visible()

    def search(self, data: str):
        expect(self.search_box).to_be_visible()
        self.search_box.fill(data)

    def edit_click(self, id: str):
        edit = self.page.locator(f'#edit-record-{id}')
        expect(edit).to_be_visible()
        edit.click()

    def edit_row_by_text(self, name: str):
        rows = self.page.locator(".rt-tr-group")
        count = rows.count()
        for i in range(count):
            row = rows.nth(i)
            text = rows.nth(i).inner_text()
            if name in text:
                edit_btn = row.locator("span[title='Edit']")
                expect(edit_btn).to_be_visible()
                edit_btn.click()

    def delete_row_by_text(self, name: str):
        rows = self.page.locator(".rt-tr-group")
        count = rows.count()
        for i in range(count):
            row = rows.nth(i)
            text = rows.nth(i).inner_text()
            if name in text:
                delete_btn = row.locator("span[title='Delete']")
                expect(delete_btn).to_be_visible()
                delete_btn.click()

    def check_data_deleted(self, row_data: list[str]):
        rows = self.page.locator(".rt-tr-group")
        count = rows.count()

        for value in row_data:
            found = True
            for i in range(count):
                text = rows.nth(i).inner_text()
                if value in text:
                    found = False
                    break
            assert found, f"Значение '{value}'  найдено в строке таблицы"
