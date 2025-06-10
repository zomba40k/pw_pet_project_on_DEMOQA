from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from faker import Faker
class AlertsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.alert_btn = self.page.locator('#alertButton')
        self.time_alert_btn = self.page.locator('#timerAlertButton')
        self.confirm_alert_btn = self.page.locator('#confirmButton')
        self.promt_alert_btn = self.page.locator('#promtButton')
        self.confirm_result = self.page.locator('#confirmResult')
        self.promt_result = self.page.locator('#promptResult')

    def click_and_check_alert_btn(self):
        alert_message = None

        def handle_alert(dialog):
            nonlocal alert_message
            alert_message = dialog.message
            dialog.dismiss()
            print(alert_message)

        self.page.once('dialog', handle_alert)
        self.alert_btn.click()
        assert alert_message == 'You clicked a button', f'Текст в алерте {alert_message}, ожидался "You clicked a button"'

    def click_and_check_time_alert_btn(self):

        with self.page.expect_event("dialog") as dialog_event:
            self.time_alert_btn.click()

        dialog = dialog_event.value
        alert_text = dialog.message


        assert alert_text == "You clicked a button", (
            f'Ожидался текст "This alert appeared after 5 seconds"", получено: "{alert_text}"'
        )
        dialog.dismiss()

    def click_and_check_confirm_alert_btn(self,option:bool=True):
        alert_message = None

        def handle_alert(dialog):

            nonlocal alert_message
            alert_message = dialog.message
            if option:
              dialog.accept()
            else:
                dialog.dismiss()
            print(alert_message)

        self.page.once('dialog', handle_alert)
        self.confirm_alert_btn.click()
        if option:
            assert self.confirm_result.text_content() == 'You selected Ok'
        else:
            assert self.confirm_result.text_content() == 'You selected Cancel'
        assert alert_message == 'Do you confirm action?', f'Текст в алерте {alert_message}, ожидался "Do you confirm action?"'

    def click_and_check_promt_alert_btn(self):
        fake = Faker()
        alert_message = None
        word = fake.word()
        def handle_alert(dialog):
            nonlocal alert_message
            alert_message = dialog.message
            dialog.accept(word)

        self.page.once('dialog', handle_alert)
        self.promt_alert_btn.click()
        assert alert_message == 'Please enter your name', f'Ожидался текст "Please enter your name", получился {alert_message}'
        expect(self.promt_result).to_contain_text(word)
