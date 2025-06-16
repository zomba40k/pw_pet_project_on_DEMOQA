import pytest
import allure

from pages.Elements.check_box import CheckBox

link = 'https://demoqa.com/checkbox'

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты чек-боксов")
@pytest.mark.Elements
class TestCheckBox:
    @allure.title("При клике на стрелочку, папка раскрывается")
    def test_expand_all_button(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.check_expand_all()

    @allure.description("При клике на '-' сворачиваются все папкивсе папки")
    def test_collapse_all_button(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.check_expand_all()
        checkbox.collapse_all()
        checkbox.check_collapse_all()

    @allure.title('При клике на чекбокс на папке/файле, отмечается сама сущность и все вложенные в нее сущности')
    def test_select_desktop_checkbox(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.select_checkbox("Desktop")
        checkbox.check_selected_result("desktop")
    @allure.title('При клике на "+" расскрываются все папки')
    def test_expand_on_a_home_folder(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_folder('Home')
        checkbox.check_folder_expanded('home')
