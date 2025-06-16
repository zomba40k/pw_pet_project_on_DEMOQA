from pages.Widgets.menu_page import MenuPage

link = 'https://demoqa.com/menu#'
class TestMenuPage:

    def test_main_item_2(self,page):
        item = MenuPage(page)
        item.open(link)
        item.hover_over(item.main_item_2_header)
        item.sub_list.is_visible()

    def test_sub_sub_list(self,page):
        sub = MenuPage(page)
        sub.open(link)
        sub.hover_over(sub.main_item_2_header)
        sub.sub_list.is_visible()
        sub.hover_over(sub.sub_sub_list_header)
        sub.sub_sub_list.is_visible()
