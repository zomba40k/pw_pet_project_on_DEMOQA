from allure_pytest.utils import allure_title

from pages.Widgets.progress_bar_page import ProgressBarPage
import pytest
import allure

link = 'https://demoqa.com/progress-bar'

@allure.parent_suite("Тесты Widgets")
@allure.suite("Тесты Progress bar")
@pytest.mark.Widgets
class TestProgressBar:
    @allure.title('По клику по кнопку Start прогресс бар над ней начинает заполняться(0-100)')
    def test_progres_bar(self,page):
        page = ProgressBarPage(page)
        page.open(link)
        progress = 25
        initial_progress_bar_value = page.current_progress_bar_value()
        page.start_and_stop_after(progress)
        final_progress_bar_value = page.current_progress_bar_value()
        assert str(int(initial_progress_bar_value) +int(progress)) ==  final_progress_bar_value,f'Прогресс бар дошел до неверного значения, ожидалось {progress}, вышло {final_progress_bar_value} '

    @allure.title('По клику по кнопку Reset  после заполнения прогресс бара, его значение сбрасывается до 0, появляется возможность заново нажать Start')
    def test_reset(self,page):
        page = ProgressBarPage(page)
        page.open(link)
        page.start()
        page.page.wait_for_timeout(10000)
        page.reset()
        assert page.current_progress_bar_value() == '0', f'Значение в прогресс баре {page.current_progress_bar_value()}, должно быть {0}'