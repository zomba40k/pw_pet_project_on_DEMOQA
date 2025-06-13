from pages.base_page import BasePage
from playwright.sync_api import expect

class TabsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.all_tabs = self.page.locator('div[id^="demo-tab"]')
        self.what_header = self.page.locator('#demo-tab-what')
        self.origin_header = self.page.locator('#demo-tab-origin')
        self.use_header = self.page.locator('#demo-tab-use')
        self.more_header = self.page.locator('#demo-tab-more')




    def is_all_tabs_present(self):
        assert self.all_tabs.count() == 4, f'Ожидалось что вкладок будет 4, но их {self.all_tabs.count()}'

    def check_is_text_visible(self,locator):
        if locator == 'what':
            expect(self.page.locator('#demo-tabpane-what')).to_have_attribute('aria-hidden','false')

        elif locator == 'origin' :
            expect(self.page.locator('#demo-tabpane-origin')).to_have_attribute('aria-hidden','false')

        elif locator == 'use':
            expect(self.page.locator('#demo-tabpane-use')).to_have_attribute('aria-hidden', 'false')

    def check_is_disabled(self, header:str='more'):
        if header == 'more':
            expect(self.page.locator('#demo-tab-more')).to_have_attribute('aria-disabled', 'true')

