from pages.Alerts_Frame_Windows.alerts_page import AlertsPage
import pytest
link = 'https://demoqa.com/alerts'
class TestAlerts():


    def test_alert_btn(self,page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_alert_btn()

    def test_time_alert_btn(self,page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_time_alert_btn()
    @pytest.mark.parametrize('option', [True, False])
    def test_confirm_alert_btn(self,page,option):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_confirm_alert_btn(option)

    def test_prompt_alert_btn(self,page):
        alert = AlertsPage(page)
        alert.open(link)
        alert.click_and_check_promt_alert_btn()
