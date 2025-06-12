from pages.Alerts_Frame_Windows.browser_windows_page import BrowserWindowsPage

link = 'https://demoqa.com/browser-windows'


class TestBrowserWindowsPage:

    def test_new_tab(self, page):
        tab = BrowserWindowsPage(page)
        tab.open(link)
        tab.click_tab_btn()

    def test_new_window(self, page):
        window = BrowserWindowsPage(page)
        window.open(link)
        window.click_window_btn()

    def test_new_window_message(self, page):
        message = BrowserWindowsPage(page)
        message.open(link)
        message.click_window_msg_btn()
