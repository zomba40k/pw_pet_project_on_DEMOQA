from playwright.sync_api import expect

from pages.base_page import BasePage


class AcordianPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_accordian(self, section_title: str = 'What', expected_text: str = 'Lorem Ipsum is simply dummy'):
        text = self.page.get_by_text(expected_text, exact=False)
        if not text.is_visible():
            section = self.page.locator(f".card-header:has-text('{section_title}')")
            section.click()
        expect(text).to_be_visible()

    def check_if_other_hidden(self):
        locators = self.page.locator('.show')
        assert locators.count() == 1, f'Должна быть раскрытой одна секция, раскрыто{locators.count()}'
