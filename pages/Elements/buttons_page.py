from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()
from pages.Elements.base_page import BasePage


class ButtonsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.db_click_btn = self.page.locator("#doubleClickBtn")
        self.rgt_click_btn = self.page.locator("#rightClickBtn")
        self.lft_click_btn = self.page.get_by_text("Click Me", exact=True)
        self.db_click_msg = self.page.locator("#doubleClickMessage")
        self.rgt_click_msg = self.page.locator("#rightClickMessage")
        self.lft_click_msg = self.page.locator('#dynamicClickMessage')

    def check_db_click(self):
        self.db_click_btn.dblclick()
        expect(self.db_click_msg).to_contain_text('You have done a double click')

    def check_rgt_click(self):
        self.rgt_click_btn.click(button='right')
        expect(self.rgt_click_msg).to_contain_text('You have done a right click')

    def check_lft_click(self):
        self.lft_click_btn.click()
        expect(self.lft_click_msg).to_contain_text('You have done a dynamic click')
