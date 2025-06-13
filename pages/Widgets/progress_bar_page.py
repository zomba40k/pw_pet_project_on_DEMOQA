from pages.base_page import BasePage
from playwright.sync_api import expect


class ProgressBarPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.start_stop_btn = self.page.locator('#startStopButton')
        self.reset_btn = self.page.locator('#resetButton')
        self.progress_bar = self.page.locator('.progress-bar')


    def start_and_stop_after(self,value):
        self.start()
        handle = self.progress_bar.element_handle()
        self.page.wait_for_function(
            """(args) => args.el.textContent.trim() === args.val + '%'""",
            arg={
                "el": handle,
                "val": str(value)
            },
            timeout=10000
        )
        self.stop()
    def start(self):
        expect(self.start_stop_btn).to_have_text('Start')
        self.start_stop_btn.click()

    def stop(self):
        expect(self.start_stop_btn).to_have_text('Stop')
        self.start_stop_btn.click()

    def current_progress_bar_value(self):
        value = self.progress_bar.get_attribute('aria-valuenow')
        return value

    def reset(self):
        expect(self.reset_btn).to_have_text('Reset')
        self.reset_btn.click()
