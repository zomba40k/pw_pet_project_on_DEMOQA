from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.enable_after_btn = self.page.locator('#enableAfter')
        self.color_change_btn = self.page.locator('#colorChange')
        self.visible_after_btn = self.page.locator('#visibleAfter')

    def check_btn_enabled(self, locator):
        expect(locator).to_be_enabled(timeout=6000)

    def check_btn_color(self, locator):
        initial_class = locator.get_attribute("class")
        expect(locator).not_to_have_class(initial_class, timeout=6000)

    def check_btn_visible(self, locator):
        expect(locator).to_be_visible(timeout=6000)
