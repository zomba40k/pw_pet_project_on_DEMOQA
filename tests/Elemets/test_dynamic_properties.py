from pages.Elements.dynamic_properties_page import DynamicPropertiesPage
import pytest
link = 'https://demoqa.com/dynamic-properties'


@pytest.mark.Elements
class TestDynamicProperties:

    def test_enable_after_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_enabled(page.enable_after_btn)

    def test_visible_after_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_visible(page.visible_after_btn)

    def test_color_change_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_color(page.color_change_btn)

    def test_all_dynamic_buttons(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_color(page.color_change_btn)
        page.check_btn_enabled(page.enable_after_btn)
        page.check_btn_visible(page.visible_after_btn)
