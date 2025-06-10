import os
from faker import Faker
from faker.providers import phone_number
from pages.Elements.base_page import BasePage
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

    def fill_fields(self):
        self.first_name.fill(fake.first_name())
        self.last_name.fill(fake.last_name())
        self.email.fill(fake.email())
        self.address.fill(fake.address())
        self.phone.fill(fake.msisdn()[:10])

    def select_gender(self,gender:str='Male'):
        self.page.locator(f'label:has-text("{gender}")').nth(0).click()


    def select_date(self, day="15", month="May", year="1990"):
        self.date_picker.click()
        self.page.locator(".react-datepicker__year-select").select_option(label=year)
        self.page.locator(".react-datepicker__month-select").select_option(label=month)
        self.page.locator(f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)").click()

    def select_subject(self,subject:str='Math'):
        self.subject_input.click()
        self.subject_input.fill(subject)
        self.page.locator(".subjects-auto-complete__option", has_text=subject).click()
        expect(self.page.locator('.subjects-auto-complete__multi-value__label', has_text=subject)).to_be_visible()

    def select_hobby(self,hobbies:list=['Sports']):
        for hobby in hobbies:
            check = self.page.locator(f'label:has-text("{hobby}")')
            check.click()
            expect(check).to_be_checked()
    def upload(self, file: str = 'test_data/testfile.txt'):
        filename = os.path.basename(file)
        self.page.locator("#uploadPicture").set_input_files(file)
        expect(self.page.locator(f"span:has-text('{filename}')")).to_be_hidden()

    def select_state(self, state_name: str=None):
        if state_name is not None:
            self.state_input.fill(state_name)
            state = self.page.locator('div[id^="react-select-3-option-"]',has_text=state_name)

        else:
            self.page.locator('#state').click()
            state = self.page.locator('div[id^="react-select-3-option-"]').all()
            state = random.choice(state)
        state.click()

    def select_city(self, city_name: str = None):
        if city_name is not None:
            state = self.page.locator('div[id^="react-select-4-option-"]', has_text=city_name)

        else:
            self.page.locator('#city').click()
            state = self.page.locator('div[id^="react-select-4-option-"]').all()
            state = random.choice(state)
        state.click()



    def fill_form(self):
        self.fill_fields()
        self.select_gender()
        self.select_date()
        self.select_subject()
        self.select_hobby()
        self.upload()
        self.select_state()
        #self.select_city()



