from pages.Widgets.tabs_page import TabsPage
import pytest

link = 'https://demoqa.com/tabs'
@pytest.mark.Widgets
class TestTabsPage:


    def test_tab(self,page):
        tabs = TabsPage(page)
        tabs.open(link)
        tabs.is_all_tabs_present()
        tabs.check_is_text_visible('what')
        tabs.click(tabs.origin_header)
        tabs.check_is_text_visible('origin')
        tabs.click(tabs.use_header)
        tabs.check_is_text_visible('use')
        tabs.check_is_disabled(tabs.more_header)
