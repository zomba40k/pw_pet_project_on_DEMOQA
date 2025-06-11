from pages.base_page import BasePage
from playwright.sync_api import expect


class AutoCompletePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.mult_color_input = page.locator("#autoCompleteMultipleInput")
        self.single_color_input = page.locator("#autoCompleteSingleInput")

    def check_color_choice(self, text: str = 'Black', multiple: bool = True):
        input_field = self.mult_color_input if multiple else self.single_color_input
        input_field.fill(text)

        # Получаем все уникальные варианты, которые появились
        options = self.page.locator('.auto-complete__option', has_text=text)
        expected_colors = options.all_text_contents()

        for _ in range(len(expected_colors)):
            # Обновляем локатор, т.к. список опций сбрасывается после клика
            self.page.wait_for_timeout(200)
            option = self.page.locator('.auto-complete__option', has_text=text)
            option.first.click()
            if not multiple:
                break
            input_field.fill(text)
            self.page.wait_for_timeout(200)
        return expected_colors


    def check_multiple_colors_added(self,expected_colors:list[str]):
        actual_colors = []
        labels = self.page.locator('.auto-complete__multi-value__label')
        for colors in range(labels.count()):
            actual_colors.append(expected_colors[colors])
        assert(sorted(actual_colors) == sorted(expected_colors)), 'Not all colors added'

    def check_single_color_added(self,expected_colors:list[str]):
        actual_color = self.page.locator('.auto-complete__single-value').text_content()
        assert expected_colors[0] == actual_color, 'Wrong color added'
