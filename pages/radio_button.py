from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()
from pages.base_page import BasePage

class RadioButton(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.yes_button = page.locator('#yesRadio')
        self.no_button = page.locator('#noRadio')
        self.impressive_button = page.locator('#impressiveRadio')
        self.succes_message = page.locator('.text-success')


    def click_radio(self,name):
        self.page.locator(f"label[for='{name}Radio']").click()

    def check_succes_message(self,name:str):
        result = self.page.locator(".text-success")
        expect(result).to_have_text(name)


    def check_no(self):
        expect(self.no_button).to_be_disabled()



