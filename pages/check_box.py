from playwright.sync_api import Page, expect, sync_playwright
from faker import Faker
fake = Faker()
from pages.base_page import BasePage
import re

class CheckBox(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.expand_all_button = page.locator(".rct-option-expand-all")
        self.collapse_all_button = page.locator(".rct-option-collapse-all")
        self.home_expand_button = page.locator("#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > span > button")
        self.checkbox_private = page.locator("#checkbox-private")
        self.result = page.locator("#result")
        self.collapsed_locator = page.locator(".rct-node-collapsed")



    def expand_all(self):
        self.expand_all_button.click()

    def check_collapse_all(self):
        expect(self.collapsed_locator).to_be_visible()

    def collapse_all(self):
        self.collapse_all_button.click()

    def select_checkbox(self, name: str):
        # Ищет чекбокс по тексту и кликает по label
        checkbox_label = self.page.locator(f"label:has-text('{name}')")
        expect(checkbox_label).to_be_visible()
        checkbox_label.click()


    def check_selected_result(self, expected_text: str):
        expect(self.result).to_contain_text(expected_text.lower())

    def check_expand_all(self):
        self.expand_all_button.click()
        expect(self.collapsed_locator).not_to_be_visible()

    def expand_folder(self, name: str):
        node = self.page.locator(f".rct-node:has(label:has-text('{name}'))")
        button = node.locator(".rct-collapse")
        expect(button).to_be_visible()
        button.click()

    def check_folder_expanded(self, name: str):
        node = self.page.locator(f".rct-node:has(label:has-text('{name}'))")
        expect(node).to_have_class(re.compile(r".*\brct-node-expanded\b.*"))

