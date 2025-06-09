from pages.practice_form_page import PracticeFormPage


link = 'https://demoqa.com/automation-practice-form'
class TestPracticeFormPage:

    def test_form(self,page):
        form = PracticeFormPage(page)
        form.open(link)
        form.fill_form()



