from pages.check_box import CheckBox

link = 'https://demoqa.com/checkbox'


class TestCheckBox:

    def test_expand_all_button(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.check_expand_all()

    def test_collapse_all_button(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.check_expand_all()
        checkbox.collapse_all()
        checkbox.check_collapse_all()

    def test_select_desktop_checkbox(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_all()
        checkbox.select_checkbox("Desktop")
        checkbox.check_selected_result("desktop")

    def test_expand_on_a_home_folder(self, page):
        checkbox = CheckBox(page)
        checkbox.open(link)
        checkbox.expand_folder('Home')
        checkbox.check_folder_expanded('home')
