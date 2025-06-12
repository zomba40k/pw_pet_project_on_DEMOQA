from pages.Widgets.accordian_page import AcordianPage

link = 'https://demoqa.com/accordian'


class TestAcordianPage:

    def test_what_is(self, page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian(expected_text='adable Engl', section_title='Why')
        accordian.check_accordian(expected_text='000 years old. Ric', section_title='Where')
        accordian.check_accordian()
