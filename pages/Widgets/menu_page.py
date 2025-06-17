from pages.base_page import BasePage

class MenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.main_item_2_header = page.locator("#nav >> text=Main Item 2")
        self.sub_list = self.page.locator("#nav > li:nth-child(2) > ul")
        self.sub_sub_list_header = self.page.locator("#nav >> text=SUB SUB LIST »")
        self.sub_sub_list = self.page.locator("#nav > li:nth-child(2) > ul > li:nth-child(3) > ul")



