from pages.Alerts_Frame_Windows.modals_page import ModalsPage

link = 'https://demoqa.com/modal-dialogs'
class TestModals:

    def test_modals(self,page):
        modals = ModalsPage(page)
        modals.open(link)
        modals.check_small_modal()
        modals.check_large_modal()

