import pytest

from pages.Alerts_Frame_Windows.alerts_page import AlertsPage
import allure

link = 'https://demoqa.com/alerts'

@allure.parent_suite("Тесты алертов фреймов и окон")
@allure.suite("Тесты алертов")
@pytest.mark.Alerts_Frame_Windows
class TestAlerts:
    @allure.title("Тест алерта")
    def test_alert_btn(self, page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_alert_btn()

    @allure.title("При клике на кнопку справа от On button click, alert will appear after 5 seconds обычный алерт появляется спустя 5 секунд")
    def test_time_alert_btn(self, page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_time_alert_btn()

    @allure.title("При клике на кнопку справа от On button click, confirm box will appearYou selected Ok появляется confirm алерт")
    @pytest.mark.parametrize('option', [True, False])
    def test_confirm_alert_btn(self, page, option):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_confirm_alert_btn(option)

    @allure.title("При клике на кнопку справа от On button click, prompt box will appear появляется prompt алерт")
    def test_prompt_alert_btn(self, page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_promt_alert_btn()
