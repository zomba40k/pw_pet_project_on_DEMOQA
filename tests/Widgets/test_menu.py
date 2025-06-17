from pages.Widgets.menu_page import MenuPage
import pytest
import allure

link = 'https://demoqa.com/menu#'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Menu page")
@pytest.mark.Widgets
class TestMenuPage:

    @allure.title('При наведении курсора на Main Item 2 в навигационной панели , выпадает список с под сущностями')
    def test_main_item_2(self,page):
        item = MenuPage(page)
        item.open(link)
        item.hover_over(item.main_item_2_header)
        item.sub_list.is_visible()

    @allure.title('При наведении курсора на под сущность SUB SUB LIST, выпадает список с сущностями')
    def test_sub_sub_list(self,page):
        sub = MenuPage(page)
        sub.open(link)
        sub.hover_over(sub.main_item_2_header)
        sub.sub_list.is_visible()
        sub.hover_over(sub.sub_sub_list_header)
        sub.sub_sub_list.is_visible()
