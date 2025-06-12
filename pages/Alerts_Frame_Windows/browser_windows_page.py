from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tab_btn = self.page.locator("#tabButton")
        self.window_btn = self.page.locator("#windowButton")
        self.message_window_btn = self.page.locator("#messageWindowButton")

    def click_tab_btn(self):
        with self.page.expect_popup() as popup_info:
            self.tab_btn.click()

        new_tab = popup_info.value
        assert new_tab.url == 'https://demoqa.com/sample'
        expect(new_tab.locator('body')).to_contain_text('This is a sample page')

    def click_window_btn(self):
        with self.page.expect_popup() as popup_info:
            self.window_btn.click()
        new_window = popup_info.value

        expect(new_window.locator('body')).to_contain_text('This is a sample page')
        assert new_window.url == 'https://demoqa.com/sample'

    def click_window_msg_btn(self):
        with self.page.expect_popup() as popup_info:
            self.message_window_btn.click()

        new_msg_window = popup_info.value
        expect(new_msg_window.locator('body')).to_contain_text('Knowledge increases by sharing but not by saving. ')
