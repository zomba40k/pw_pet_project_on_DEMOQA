from pages.Elements.dynamic_properties_page import DynamicPropertiesPage
import pytest
import allure
link = 'https://demoqa.com/dynamic-properties'

@allure.parent_suite("Тесты Elements")
@allure.suite("Тесты динамических свойств")
@pytest.mark.Elements
class TestDynamicProperties:
    @pytest.fixture(autouse=True)
    def setup(self,page):
        self.dynamic = DynamicPropertiesPage(page)

    @allure.title('Первая кнопка станет активной только через 5 секунда')
    def test_enable_after_btn(self):
        self.dynamic.open(link)
        self.dynamic.check_btn_enabled(self.dynamic.enable_after_btn)

    @allure.title('Третья кнопка стнет видимой через 5 секунд')
    def test_visible_after_btn(self):
        self.dynamic.open(link)
        self.dynamic.check_btn_visible(self.dynamic.visible_after_btn)

    @allure.title('Вторая кнопка поменяет цвет через  5 секунд')
    def test_color_change_btn(self):
        self.dynamic.open(link)
        self.dynamic.check_btn_color(self.dynamic.color_change_btn)
