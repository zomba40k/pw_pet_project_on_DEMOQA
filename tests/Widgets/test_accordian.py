from pages.Widgets.accordian_page import AcordianPage
import pytest
link = 'https://demoqa.com/accordian'

@pytest.mark.Widgets
class TestAcordianPage:

    def test_what_is(self, page):
        accordian = AcordianPage(page)
        accordian.open(link)


        accordian.check_accordian()

    def test_why_does(self,page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian(expected_text='000 years old. Ric', section_title='Where')
        accordian.check_if_other_hidden()

    def test_where_is(self, page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian(expected_text='adable Engl', section_title='Why')