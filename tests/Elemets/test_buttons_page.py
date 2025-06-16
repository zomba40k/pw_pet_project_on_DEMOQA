import pytest
from pages.Elements.buttons_page import ButtonsPage
import allure

link = ('https://demoqa.com/buttons')

@allure.parent_suite("Тесты элементов")
@allure.suite("Тесты клика по кнопке")
@pytest.mark.Elements
class TestButtonsPage:

    @allure.title("Двойной клик по кнопке")
    def test_dbl_click(self, page):
        page = ButtonsPage(page)
        page.open(link)
        try:
            page.check_db_click()
        except AssertionError as e:
            allure.attach(page.screenshot(), name="screenshot_dbl_click", attachment_type=allure.attachment_type.PNG)
            raise

    @allure.title("Правый клик по кнопке")
    def test_rgt_click(self, page):
        page = ButtonsPage(page)
        page.open(link)
        try:
            page.check_rgt_click()
        except AssertionError as e:
            allure.attach(page.screenshot(), name="screenshot_rgt_click", attachment_type=allure.attachment_type.PNG)
            raise

    @allure.title("Левый клик по кнопке")
    def test_lft_click(self, page):
        page = ButtonsPage(page)
        page.open(link)
        try:
            page.check_lft_click()
        except AssertionError as e:
            allure.attach(page.screenshot(), name="screenshot_lft_click", attachment_type=allure.attachment_type.PNG)
            raise