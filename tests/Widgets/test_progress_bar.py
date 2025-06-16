from pages.Widgets.progress_bar_page import ProgressBarPage
import pytest

link = 'https://demoqa.com/progress-bar'
@pytest.mark.Widgets
class TestProgressBar:

    def test_progres_bar(self,page):
        page = ProgressBarPage(page)
        page.open(link)
        progress = 25
        initial_progress_bar_value = page.current_progress_bar_value()
        page.start_and_stop_after(progress)
        final_progress_bar_value = page.current_progress_bar_value()
        assert str(int(initial_progress_bar_value) +int(progress)) ==  final_progress_bar_value,f'Прогресс бар дошел до неверного значения, ожидалось {progress}, вышло {final_progress_bar_value} '


    def test_reset(self,page):
        page = ProgressBarPage(page)
        page.open(link)
        page.start()
        page.page.wait_for_timeout(10000)
        page.reset()
        assert page.current_progress_bar_value() == '0', f'Значение в прогресс баре {page.current_progress_bar_value()}, должно быть {0}'