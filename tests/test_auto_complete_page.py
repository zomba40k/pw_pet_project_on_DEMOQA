from pages.Widgets.auto_complete_page import AutoCompletePage

link = 'https://demoqa.com/auto-complete'
class TestAutoCompletePage:

    def test_multiple_color(self,page):
        color = AutoCompletePage(page)
        color.open(link)
        selected = color.check_color_choice('a')
        color.check_multiple_colors_added(selected)


    def test_single_color(self,page):
        color = AutoCompletePage(page)
        color.open(link)
        selected = color.check_color_choice('b',multiple=False)
        color.check_single_color_added(selected)




