from playwright.sync_api import expect

from pages.base_page import BasePage


class FramesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_frame1(self):
        self.page.locator('#frame1').wait_for(state='attached')
        frame1 = None
        for _ in range(10):  # максимум 10 попыток
            frame1 = self.page.frame(name="frame1")
            if frame1:
                break
            self.page.wait_for_timeout(500)  # подождать чуть-чуть
        assert frame1 is not None, 'Frame is not found'
        expect(frame1.locator('#sampleHeading')).to_contain_text('This is a sample page')

    def check_frame2(self):
        self.page.locator('#frame2').wait_for(state='attached')
        frame2 = None
        for _ in range(10):
            frame2 = self.page.frame(name="frame2")
            if frame2:
                break
            self.page.wait_for_timeout(500)

        assert frame2 is not None, 'Frame2 is not found'
        expect(frame2.locator('#sampleHeading')).to_contain_text('This is a sample page')
