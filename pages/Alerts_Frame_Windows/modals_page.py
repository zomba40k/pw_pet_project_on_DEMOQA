from playwright.sync_api import expect
from pages.base_page import BasePage


class ModalsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.small_modal_btn = self.page.locator('#showSmallModal')
        self.large_modal_btn = self.page.locator('#showLargeModal')
        self.modal = self.page.locator('.modal-dialog')
        self.modal_header = self.page.locator('.modal-title')
        self.modal_body = self.page.locator('.modal-body')
        self.close_btn = self.page.locator('//button[contains(@id, "close")]')

    def check_small_modal(self):
        self.small_modal_btn.click()
        expect(self.modal).to_be_visible()
        expect(self.modal).to_contain_class('modal-sm')
        expect(self.modal_header).to_contain_text('Small Modal')
        expect(self.modal_body).to_contain_text('This is a small modal. It has very less content')
        self.close_btn.click()

    def check_large_modal(self):
        self.large_modal_btn.click()
        expect(self.modal).to_be_visible()
        expect(self.modal).to_contain_class('modal-lg')
        expect(self.modal_header).to_contain_text('Large Modal')
        expect(self.modal_body).to_contain_text('Lorem Ipsum')
        self.close_btn.click()
