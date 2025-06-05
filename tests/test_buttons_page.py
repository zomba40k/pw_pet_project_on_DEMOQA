from pages.buttons_page import ButtonsPage
import pytest


link = 'https://demoqa.com/buttons'
class TestButtonsPage:

    def test_dbl_click(self,page):
        page = ButtonsPage(page)
        page.open(link)
        page.check_db_click()

    def test_rgt_click(self,page):
        page = ButtonsPage(page)
        page.open(link)
        page.check_rgt_click()

    def test_lft_click(self,page):
        page = ButtonsPage(page)
        page.open(link)
        page.check_lft_click()
    @pytest.mark.smoke
    def test_all_buttons(self,page):
        page = ButtonsPage(page)
        page.open(link)
        page.check_db_click()
        page.check_rgt_click()
        page.check_lft_click()