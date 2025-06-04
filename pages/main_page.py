from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.banner = page.locator('div.home-banner > a')
        self.cards =  page.locator(".card.mt-4.top-card")

    def click_cards(self, name:str=None):


        if name == 'elements':
            self.cards.nth(0).click()

        elif name == 'forms':
            self.cards.nth(1).click()

        elif name == 'alerts':
            self.cards.nth(2).click()

        elif name == 'widgets':
            self.cards.nth(3).click()

        elif name == 'interactions':
            self.cards.nth(4).click()

        elif name == None:
            self.cards.nth(0).click()

    def is_banner_present(self):
        self.is_element_present(self.banner)