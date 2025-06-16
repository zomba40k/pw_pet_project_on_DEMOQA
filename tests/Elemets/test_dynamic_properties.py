from pages.Elements.dynamic_properties_page import DynamicPropertiesPage
import pytest
import allure
link = 'https://demoqa.com/dynamic-properties'

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты динамических свойств")
@pytest.mark.Elements
class TestDynamicProperties:
    @allure.title('Первая кнопка станет активной только через 5 секунда')
    def test_enable_after_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_enabled(page.enable_after_btn)

    @allure.title('Третья кнопка стнет видимой через 5 секунд')
    def test_visible_after_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_visible(page.visible_after_btn)

    @allure.title('Вторая кнопка поменяет цвет через  5 секунд')
    def test_color_change_btn(self, page):
        page = DynamicPropertiesPage(page)
        page.open(link)
        page.check_btn_color(page.color_change_btn)
