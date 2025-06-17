import pytest
from pages.Widgets.select_menu_page import SelectMenuPage
import allure

link = 'https://demoqa.com/select-menu'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Select menu")
@pytest.mark.Widgets
class TestSelectMenuPage:
    @allure.title('При клике по полю с заголовком Select One, выпадает список, можно произвести поиск и выбрать один префикс')
    def test_select_one_dropdown(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.select_one_field.click()
        select_page.select_option_by_partial_text("selectOne", "Pro")
        select_page.expect_selected_value("selectOne", "Prof.")

    @allure.title('При клике по полю с заголовком Select Value, можно произвести поиск и выбрать один элемент ')
    def test_select_value_dropdown(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.select_value_field.click()
        select_page.select_option_by_partial_text("selectValue", "Another")
        select_page.expect_selected_value("selectValue", "Another")

    @allure.title('По клику по полю с заголовком Old Style Select Menu выпадает список  элемент которого можно выбрать')
    def test_old_style_select(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.select_old_style("Green")
        select_page.expect_selected_old_style("Green")

    @allure.title('При клике по полю с заголовком Multi select dropdown, можно произвести поиск и выбрать один элемент ')
    def test_multiselect_dropdown_single_selection(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.multiselect_field.click()
        select_page.page.set_default_timeout(2000)
        select_page.select_option_by_partial_text("multiSelect", "Blu")
        select_page.expect_multiselect_selected(["Blue"])

    @allure.title('При клике по полю с заголовком Multi select dropdown, можно произвести поиск и выбрать несколько элементов ')
    def test_multiselect_dropdown_multi_selection(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.multiselect_field.click()
        select_page.select_option_by_partial_text("multiSelect", "Gre")
        select_page.select_option_by_partial_text("multiSelect", "Red")
        select_page.expect_multiselect_selected(["Green", "Red"])

    @allure.title('Выбранные элементы из списка Multi select dropdown можно удалить нажав на крестик справа в выбранном элементе')
    def test_multiselect_remove_single(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.multiselect_field.click()
        select_page.select_option_by_partial_text("multiSelect", "Red")
        select_page.remove_multiselect_item("Red")
        select_page.expect_multiselect_selected([])

    @allure.title('Поле Multi select dropdown можно полность очистить нажав на крестик справа в поле')
    def test_multiselect_clear_all(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.multiselect_field.click()
        select_page.select_option_by_partial_text("multiSelect", "Blue")
        select_page.select_option_by_partial_text("multiSelect", "Green")
        select_page.clear_all_multiselect()
        select_page.expect_multiselect_selected([])

    @allure.title('Тест стандартного Multi select, можно выбрать один или несколько элементов')
    def test_standard_multiselect(self,page):
        select_page = SelectMenuPage(page)
        select_page.open(link)
        select_page.select_standard_multi(["Volvo"])
        select_page.page.keyboard.down('Shift')
        select_page.expect_standard_multiselect(["Volvo"])
