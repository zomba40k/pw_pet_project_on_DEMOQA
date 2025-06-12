import os
from faker import Faker
from faker.providers import phone_number
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import random

fake = Faker()
fake.add_provider(phone_number)
class PracticeFormPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        self.first_name = self.page.locator('#firstName')
        self.last_name = self.page.locator('#lastName')
        self.email = self.page.locator('#userEmail')
        self.date_picker = self.page.locator("#dateOfBirthInput")
        self.phone = self.page.locator('#userNumber')
        self.upload_btn = self.page.locator('#uploadPicture')
        self.subject_input = self.page.locator('#subjectsInput')
        self.address = self.page.locator('#currentAddress')
        self.state_input = self.page.locator('#react-select-3-input')
        self.city_input = self.page.locator('#react-select-4-input')
        self.submit_btn = self.page.locator('#submit')
        self.modal = self.page.locator(".modal-content")
        self.modal_close_btn = self.page.locator("#closeLargeModal")

    def fill_fields(self):
        self.first_name.fill(fake.first_name())
        self.last_name.fill(fake.last_name())
        self.email.fill(fake.email())
        self.address.fill(fake.address())
        self.phone.fill(fake.msisdn()[:10])

    def select_options(self):
        self.select_date()
        self.select_subject()
        self.select_hobby()
        self.upload()
        self.select_state()
        self.select_city()

    def fill_first_name(self):
        name = fake.first_name()
        self.first_name.fill(name)
        return name

    def fill_last_name(self):
        surname  = fake.last_name()
        self.last_name.fill(surname)
        return surname

    def fill_email(self):
        email = fake.email()
        self.email.fill(email)
        return email

    def fill_address(self):
        address = fake.address()
        self.address.fill(address)
        return address

    def fill_phone(self):
        number = fake.msisdn()[:10]
        self.phone.fill(number)
        return number

    def select_gender(self,gender:str='Male'):
        self.page.locator(f'label:has-text("{gender}")').first.click()
        return self.page.locator(f'label:has-text("{gender}")').first.text_content()

    def select_date(self, day="5", month="May", year="1990"):
        self.date_picker.click()
        self.page.locator(".react-datepicker__year-select").select_option(label=year)
        self.page.locator(".react-datepicker__month-select").select_option(label=month)
        self.page.locator(f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)").click()
        return day, month, year

    def select_subject(self,subject:str='Math'):
        self.subject_input.click()
        self.subject_input.fill(subject)
        self.page.locator(".subjects-auto-complete__option", has_text=subject).click()
        expect(self.page.locator('.subjects-auto-complete__multi-value__label', has_text=subject)).to_be_visible()
        return subject

    def select_hobby(self,hobbies:list=['Sports']):
        for hobby in hobbies:
            check = self.page.locator(f'label:has-text("{hobby}")')
            check.click()
            expect(check).to_be_checked()

        return hobbies

    def upload(self, file: str = 'test_data/testfile.txt'):
        filename = os.path.basename(file)
        self.page.locator("#uploadPicture").set_input_files(file)
        expect(self.page.locator(f"span:has-text('{filename}')")).to_be_hidden()
        return filename

    def select_state(self, state_name: str=None):
        if state_name is not None:
            self.state_input.fill(state_name)
            state = self.page.locator('div[id^="react-select-3-option-"]',has_text=state_name)

        else:
            self.page.locator('#state').click()
            state = self.page.locator('div[id^="react-select-3-option-"]').all()
            state = random.choice(state)
            state_text = state.text_content()
        state.click()
        return state_text

    def select_city(self, city_name: str = None):
        if city_name is not None:
            city = self.page.locator('div[id^="react-select-4-option-"]', has_text=city_name)

        else:
            self.page.locator('#city').click()
            city = self.page.locator('div[id^="react-select-4-option-"]').all()
            city = random.choice(city)
            city_text = city.text_content()
        city.click()

        return city_text

    def fill_form(self):
        self.fill_fields()
        self.select_gender()
        self.select_date()
        self.select_subject()
        self.select_hobby()
        self.upload()
        self.select_state()
        self.select_city()

    def fill_form_invalid(self, invalid_data: dict, error_field: str):
        """
        invalid_data — словарь с полями, которые нужно заполнить вручную (в том числе некорректно),
        error_field — название поля, валидность которого проверяется.
        """

        # Только то, что указано явно (возможно, невалидно)
        if "first_name" in invalid_data:
            self.first_name.fill(invalid_data["first_name"])
        if "last_name" in invalid_data:
            self.last_name.fill(invalid_data["last_name"])
        if "email" in invalid_data:
            self.email.fill(invalid_data["email"])
        if "address" in invalid_data:
            self.address.fill(invalid_data["address"])
        if "phone" in invalid_data:
            self.phone.fill(invalid_data["phone"])
        if "gender" in invalid_data:
            if invalid_data["gender"] is not None:
                self.select_gender(invalid_data["gender"])
            # если gender=None — значит не выбирать вообще

        # Остальные поля — для прохождения формы (валидные по умолчанию)
        self.select_date()
        self.select_subject()
        self.select_hobby()
        self.upload()
        self.select_state()
        self.select_city()

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "gender": self.page.locator('input[name="gender"]').first
        }.get(error_field, None)

    def is_modal_visible(self):

        return self.modal.is_visible()

    def verify_modal_data(self, expected_data):
        assert self.is_modal_visible(), 'Модальное окно с данными студента не появилось'
        modal_data = self.page.locator(".modal-content table tbody tr")
        for i in range(modal_data.count()):
            row = modal_data.nth(i)
            label = row.locator("td").nth(0).text_content().strip()
            value = row.locator("td").nth(1).text_content().strip()

            if label == "Student Name":
                assert value == f"{expected_data['first_name']} {expected_data['last_name']}", f"Ожидалось: {expected_data['first_name']} {expected_data['last_name']}, получено: {value}"
            elif label == "Student Email":
                assert value == expected_data['email'], f"Ожидалось: {expected_data['email']}, получено: {value}"
            elif label == "Gender":
                assert value == expected_data['gender'], f"Ожидалось: {expected_data['gender']}, получено: {value}"
            elif label == "Mobile":
                assert value == expected_data['phone'], f"Ожидалось: {expected_data['phone']}, получено: {value}"
            elif label == "Date of Birth":
                day = expected_data['date'][0].zfill(2)
                assert value == f"{day} {expected_data['date'][1]},{expected_data['date'][2]}", f"Ожидалось: {expected_data['date'][0]} {expected_data['date'][1]}, {expected_data['date'][2]}, получено: {value}"
            elif label == "Subjects":
                assert expected_data['subject'] in value, f"Ожидалось, что {expected_data['subject']} будет в {value}"
            elif label == "Hobbies":
                assert value == ", ".join(
                    expected_data['hobbies']), f"Ожидалось: {', '.join(expected_data['hobbies'])}, получено: {value}"
            elif label == "Picture":
                assert value == expected_data['picture'], f"Ожидалось: {expected_data['picture']}, получено: {value}"
            elif label == "Address":
                assert value == expected_data['address'], f"Ожидалось: {expected_data['address']}, получено: {value}"
            elif label == "State and City":
                assert value == f"{expected_data['state']} {expected_data['city']}", f"Ожидалось: {expected_data['state']} {expected_data['city']}, получено: {value}"

    def close_modal(self):
        self.modal_close_btn.click()

