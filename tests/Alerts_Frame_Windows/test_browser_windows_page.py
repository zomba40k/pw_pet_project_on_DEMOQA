import allure

from pages.Alerts_Frame_Windows.browser_windows_page import BrowserWindowsPage
import pytest
link = 'https://demoqa.com/browser-windows'

@allure.parent_suite("Тесты Alerts Frames and Windows")
@allure.suite("Тесты окон и вкладок")
@pytest.mark.Alerts_Frame_Windows
class TestBrowserWindowsPage:
    @allure.title("При клике по New Tab открывается Sample page в новой кладке")
    def test_new_tab(self, page):
        tab = BrowserWindowsPage(page)
        tab.open(link)
        tab.click_tab_btn()
    @allure.title("При клике по New Window открывается Sample page в новом окне")
    def test_new_window(self, page):
        window = BrowserWindowsPage(page)
        window.open(link)
        window.click_window_btn()
    @allure.title('При клике по New Window Message открывается информационное сообщение ')
    def test_new_window_message(self, page):
        message = BrowserWindowsPage(page)
        message.open(link)
        message.click_window_msg_btn()
