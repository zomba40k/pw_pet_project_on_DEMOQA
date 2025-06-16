from pages.base_page import BasePage
from playwright.sync_api import expect

class ToolTipsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.tip_btn = self.page.locator('#toolTipButton')
        self.text_field = self.page.locator('#texFieldToolTopContainer')
        self.contrary_text = self.page.locator('a', has_text='Contrary')
        self.numbers_text = self.page.locator('a', has_text='1.10.32')
        self.tooltip = self.page.locator('.tooltip-inner')


    def check_tip(self,element:str='Button'):
        expect(self.tooltip).to_have_text(f'You hovered over the {element}')




