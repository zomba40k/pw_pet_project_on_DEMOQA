from playwright.sync_api import expect

from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_parent_frame(self):
        self.page.locator('#frame1').wait_for(state='attached')
        parent_frame = None
        for _ in range(10):
            parent_frame = self.page.frame(name='frame1')
            if parent_frame:
                break

            self.page.wait_for_timeout(500)

        assert (parent_frame is not None), 'Parent frame not found'
        expect(parent_frame.locator('body')).to_contain_text('Parent frame')
        return parent_frame

    def check_child_frame(self, parent_frame):
        parent_frame.locator('iframe').wait_for(state='attached')

        child_frame = None
        for _ in range(10):

            frames = parent_frame.child_frames
            if frames:
                child_frame = frames[0]
                break
            self.page.wait_for_timeout(500)

        assert (child_frame is not None), 'Child frame not found'
        expect(child_frame.locator('p')).to_contain_text('Child Iframe')
