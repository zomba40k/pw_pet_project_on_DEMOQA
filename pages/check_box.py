from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()
from pages.base_page import BasePage

class CheckBox(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.expand_all_button = page.locator(".rct-option-expand-all")
        self.collapse_all_button = page.locator(".rct-option-collapse-all")
        self.home_expand_button = page.locator("#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > span > button")
        self.checkbox_private = page.locator("#checkbox-private")
        self.result = page.locator("#result")


    def open(self):
        self.page.goto('https://demoqa.com/checkbox', wait_until="domcontentloaded", timeout=60000)

    def expand_all(self):
        self.expand_all_button.click()
    def collapse_all(self):
        self.collapse_all_button.click()

    def select_checkbox(self, name: str):
        # Ищет чекбокс по тексту и кликает по label
        checkbox_label = self.page.locator(f"label:has-text('{name}')")
        expect(checkbox_label).to_be_visible()
        checkbox_label.click()

    def check_selected_result(self, expected_text: str):
        expect(self.result).to_contain_text(expected_text.lower())
