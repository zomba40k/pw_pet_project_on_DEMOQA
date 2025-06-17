from faker import Faker
from playwright.sync_api import Page
from pages.base_page import BasePage

fake = Faker()

class LinksPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.home_link = self.page.locator('#simpleLink')
        self.home_link2 = self.page.locator('#dynamicLink')
        self.created_link = self.page.locator('#created')
        self.no_content_link = self.page.locator('#no-content')
        self.moved_link = self.page.locator('#moved')
        self.bad_request_link = self.page.locator('#bad-request')
        self.unauthorized_link = self.page.locator('#unauthorized')
        self.forbidden_link = self.page.locator('#forbidden')
        self.not_found_link = self.page.locator('#invalid-url')
        self.link_response = self.page.locator('#linkResponse')

    def check_home_link(self, element):
        with self.page.context.expect_page() as new_tab:
            element.click()

        new_tab = new_tab.value

        assert new_tab.url == 'https://demoqa.com/'

    def check_api_respone(self, element, status_code: int, status_message: str, endpoint: str):
        with self.page.expect_response(f'**/{endpoint}') as response_info:
            element.click()

        response = response_info.value
        assert response.status == status_code
        assert response.status_text == status_message

        msg = self.link_response.text_content()
        assert msg is not None
        assert str(status_code) in msg
        assert status_message in msg
