from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()

class TextBox:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("#userName")
        self.email_input = page.locator("#userEmail")
        self.address_input = page.locator("#currentAddress")
        self.perm_address = page.locator("#permanentAddress")  # Переименовал для единообразия
        self.submit_button = page.locator("#submit")
        self.output = page.locator("#output")
    def open(self):
        self.page.goto('https://demoqa.com/text-box', wait_until="domcontentloaded", timeout=60000)

    def is_all_elements_present(self):
        expect(self.name_input).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.address_input).to_be_visible()
        expect(self.perm_address).to_be_visible()
        expect(self.submit_button).to_be_visible()

    def submit_form_valid(self):
        fake = Faker()
        name = fake.first_name()
        email = fake.email()
        address = fake.street_address()
        perm_address = fake.street_address()
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.address_input.fill(address)
        self.perm_address.fill(perm_address)
        self.submit_button.click()
        return name, email, address, perm_address

    def success_message_doesnt_appear(self):
        expect(self.success_message).not_to_be_visible()

    def check_success_message(self,name, email, address, perm_address):
        self.page.wait_for_selector("#output", timeout=10000)
        expect(self.output).to_be_visible(timeout=10000)
        expect(self.output.locator("#name")).to_contain_text(name)
        expect(self.output.locator("#email")).to_contain_text(email)
        expect(self.output.locator("#currentAddress")).to_contain_text(address)
        expect(self.output.locator("#permanentAddress")).to_contain_text(perm_address)

    #Отправка формы с пустым значением
    def submit_form_custom(self,field:str,custom_value:str):
        fake = Faker()
        # Сначала сгенерим значения
        name = fake.first_name()
        email = fake.email()
        address = fake.street_address()
        perm_address = fake.street_address()

        # Заменим одно из значений, если указано
        if field == "name":
            name = custom_value
        elif field == "email":
            email = custom_value
        elif field == "current_address":
            address = custom_value
        elif field == "perm_address":
            perm_address = custom_value
        else:
            raise ValueError(f"Unknown field: {field}")

        # Заполним форму
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.address_input.fill(address)
        self.perm_address.fill(perm_address)
        self.submit_button.click()

        return name, email, address, perm_address

    def check_field_has_error(self, field_locator):
        class_list = field_locator.get_attribute("class")
        assert class_list is not None, "Атрибут class не найден"
        assert 'field-error' in class_list.split(), f"Ожидалось что класс имеет field-error, но получили: {class_list}"