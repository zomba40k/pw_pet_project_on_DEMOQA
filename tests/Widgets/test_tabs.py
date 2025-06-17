from pages.Widgets.tabs_page import TabsPage
import pytest
import allure
link = 'https://demoqa.com/tabs'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Слайдера")
@pytest.mark.Widgets
class TestTabsPage:
    @allure.title('Тест можно ли расскрыть вкладку')
    def test_tab_can_be_open(self,page):
        tabs = TabsPage(page)
        tabs.open(link)
        tabs.is_all_tabs_present()
        tabs.check_is_text_visible('what')
        tabs.click(tabs.origin_header)
        tabs.check_is_text_visible('origin')
        tabs.click(tabs.use_header)
        tabs.check_is_text_visible('use')

    @allure.title('Вкладка more недоступна')
    def test_more_is_disabled(self,page):
        tabs = TabsPage(page)
        tabs.open(link)
        tabs.check_is_disabled(tabs.more_header)
