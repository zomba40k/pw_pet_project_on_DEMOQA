from pages.base_page import BasePage
from playwright.sync_api import expect

class SelectMenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.select_value_field = page.locator("#withOptGroup")
        self.select_one_field = page.locator("#selectOne")
        self.multiselect_field = page.get_by_text('Select...')
        self.standard_multi = page.locator("#cars")
        self.old_style = page.locator("#oldSelectMenu")
        self.clear_all = page.locator("[class*=indicatorContainer]").nth(2)


    def select_option_by_partial_text(self, field, partial_text):
        self.page.locator("div[id^='react-select']",has_text=partial_text).click()

    def expect_selected_value(self, field, expected):
        selected = self.page.locator("[class*='singleValue']")
        expect(selected).to_contain_text(expected)

    def select_old_style(self, value):
        self.old_style.select_option(label=value)

    def expect_selected_old_style(self, label):
        selected_option = self.page.locator("#oldSelectMenu option:checked")
        expect(selected_option).to_have_text(label)
    def expect_multiselect_selected(self, expected):
        self.page.wait_for_timeout(500)
        tags = self.page.locator(".css-1rhbuit-multiValue")
        tag_texts = tags.all_inner_texts()
        assert set(tag_texts) == set(expected)

    def remove_multiselect_item(self, value):
        self.page.wait_for_timeout(200)
        self.page.locator(f".css-1rhbuit-multiValue:has-text('{value}') svg").click()

    def clear_all_multiselect(self):
        self.clear_all.click()

    def select_standard_multi(self, values: list):
        self.page.keyboard.down('Control')
        for val in values:
            self.standard_multi.select_option(label=val)
        self.page.keyboard.up('Control')

    def expect_standard_multiselect(self, expected):
        selected = self.standard_multi.evaluate("el => Array.from(el.selectedOptions).map(o => o.label)")
        assert set(selected) == set(expected)
