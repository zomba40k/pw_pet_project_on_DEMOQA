from pages.base_page import BasePage
from playwright.sync_api import Page, expect, sync_playwright

class BrokenLinksPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        self.valid_image = self.page.locator("p:has-text('Valid image') + img")
        self.broken_image = self.page.locator("p:has-text('Broken image') + img")
        self.valid_link = self.page.get_by_text('Click Here for Valid Link')
        self.broken_link = self.page.get_by_text('Click Here for Broken Link')

    def is_image_valid(self,locator):
        expect(locator).to_be_visible()
        assert   locator.evaluate('''el => !el.complete || el.naturalWidth > 0'''), 'Image broken'
    def is_image_not_broken(self,locator):
        expect(locator).to_be_visible()
        assert locator.evaluate('''el => !el.complete || el.naturalWidth == 0'''), 'Image not broken'

    def check_valid_link(self):
        self.valid_link.click()
        assert self.page.url == 'https://demoqa.com/'

    def check_broken_link(self):
        status_code = None
        url = 'http://the-internet.herokuapp.com/status_codes/500'


        def handle_response(response):
            nonlocal status_code
            if response.url in url:
                status_code = response.status

        self.page.on('response', handle_response)
        self.broken_link.click()
        self.page.wait_for_load_state('networkidle')

        assert status_code is not None, 'Failed to capture response for the broken link'
        assert status_code == 500, f'Expected 500 but got {status_code}'
        assert self.page.url == url, f'Expected {url} but got {self.page.url}'

