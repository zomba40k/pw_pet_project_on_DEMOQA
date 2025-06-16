from playwright.sync_api import Page, expect
import pytest

class BasePage():
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator('header > a')
        self.lists = page.locator(".group-header")
        self.sections = page.locator(".element-list")
        self.right_banner_img = page.locator("#RightSide_Advertisement  img")

    def open(self, link: str, ):
        self.page.route("**/*stats.g.doubleclick.net/**", lambda route: route.abort())

        def handle_response(response):
            if response.status == 502:
                pytest.xfail(f"Page {link} returned 502 Bad Gateway")

        self.page.on("response", handle_response)

        self.page.goto(link, wait_until="domcontentloaded", timeout=60000)

    def check_field_has_error(self, field_locator):
        is_valid = field_locator.evaluate("el => el.checkValidity()")
        assert is_valid is False, "Ожидалось, что поле невалидно, но оно прошло валидацию"

    def is_element_present(self, element):
        try:
            expect(element).to_be_visible()
        except AssertionError:
            raise AssertionError(f'Element is not visible')

    def check_logo(self):
        expect(self.logo).to_be_visible()

    def click_logo(self):
        self.logo.click()

    def check_page(self, name: str = None):
        if name == None:
            assert self.page.url == 'https://demoqa.com/'
        else:
            assert self.page.url == f'https://demoqa.com/{name}'

    def check_lists_can_collapse(self):
        count = self.lists.count()
        for i in range(count):
            list_header = self.lists.nth(i)
            section = self.sections.nth(i)
            if i == 0:  # Первый список развёрнут
                # Проверяем точный класс
                expect(section).to_have_class("element-list collapse show")
                list_header.click()
                expect(section).to_have_class("element-list collapse")
            else:  # Остальные свёрнуты
                list_header.click()
                expect(section).to_have_class("element-list collapse show")
                list_header.click()
                expect(section).to_have_class("element-list collapse")

    def check_banner_right(self):
        expect(self.right_banner_img).to_be_visible()
        assert int(self.right_banner_img.evaluate('el => el.naturalWidth')) > 0, 'Banner is not visible'

    def select_from_sidebar(self, name: str = 'Check Box'):
        item = self.page.get_by_text(name, exact=True)

        if not item.is_visible():
            # Раскрываем секцию, внутри которой находится нужный пункт
            section = self.page.locator(f".element-group:has-text('{name}')")
            section.locator(".group-header").click()

        item.click()

    def click(self, locator):
        locator.click()

    def hover_over(self,element):
        self.page.wait_for_timeout(200)
        element.hover()