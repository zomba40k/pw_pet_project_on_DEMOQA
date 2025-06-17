from pages.Widgets.accordian_page import AcordianPage
import pytest
import allure
link = 'https://demoqa.com/accordian'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты аккордионов")
@pytest.mark.Widgets
class TestAcordianPage:

    @allure.title('При открытии страницы отображается аккордион What is lorem ipsum')
    def test_what_is(self, page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian()

    @allure.title('Нажав на аккордион Where does it come from? он раскрывается')
    def test_why_does(self,page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian(expected_text='000 years old. Ric', section_title='Where')
        accordian.check_if_other_hidden()

    @allure.title('Нажав на аккордион Why do we use it? он раскрывается')
    def test_where_is(self, page):
        accordian = AcordianPage(page)
        accordian.open(link)
        accordian.check_accordian(expected_text='adable Engl', section_title='Why')