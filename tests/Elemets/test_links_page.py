import pytest

from pages.Elements.links_page import LinksPage

link = 'https://demoqa.com/links'


@pytest.mark.Elements
class TestLinksPage:

    def test_home_link(self, page):
        page = LinksPage(page)
        page.open(link)
        page.check_home_link(page.home_link)

    def test_home_link2(self, page):
        page = LinksPage(page)
        page.open(link)
        page.check_home_link(page.home_link2)

    @pytest.mark.parametrize(
        "link_attr, status_code, status_text, endpoint",
        [
            ("created_link", 201, "Created", "created"),
            ("no_content_link", 204, "No Content", "no-content"),
            ("moved_link", 301, "Moved Permanently", "moved"),
            ("bad_request_link", 400, "Bad Request", "bad-request"),
            ("unauthorized_link", 401, "Unauthorized", "unauthorized"),
            ("forbidden_link", 403, "Forbidden", "forbidden"),
            ("not_found_link", 404, "Not Found", "invalid-url"),
        ])
    def test_api_links(self, page, link_attr, status_code, status_text, endpoint):
        page = LinksPage(page)
        page.open("https://demoqa.com/links")

        # Получаем локатор по имени атрибута
        link_element = getattr(page, link_attr)

        page.check_api_respone(link_element, status_code, status_text, endpoint)
