from pages.Widgets.auto_complete_page import AutoCompletePage
import pytest
import allure
link = 'https://demoqa.com/auto-complete'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Автозаполнения")
@pytest.mark.Widgets
class TestAutoCompletePage:

    @allure.title('Тест в поле с множественным можно воспроизвести поиск по цветам и выбрать нужный')
    def test_multiple_color(self, page):
        color = AutoCompletePage(page)
        color.open(link)
        selected = color.check_color_choice('a')
        color.check_multiple_colors_added(selected)

    @allure.title('Тест цвет можно удалить из поля множественного выбора')
    def test_color_can_be_deleted(self, page):
        color = AutoCompletePage(page)
        color.open(link)
        selected = color.check_color_choice('a')
        color.check_multiple_colors_added(selected)
        color.delete_color()
        color.is_color_deleted(selected)

    @allure.title('Тест в поле с одиночным можно воспроизвести поиск по цветам и выбрать нужный')
    def test_single_color(self, page):
        color = AutoCompletePage(page)
        color.open(link)
        selected = color.check_color_choice('b', multiple=False)
        color.check_single_color_added(selected)
