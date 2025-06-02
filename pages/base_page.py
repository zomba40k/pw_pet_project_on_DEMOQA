from playwright.sync_api import Page, expect
class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def check_field_has_error(self, field_locator):
        class_list = field_locator.get_attribute("class")
        assert class_list is not None, "Атрибут class не найден"
        assert 'field-error' in class_list.split(), f"Ожидалось что класс имеет field-error, но получили: {class_list}"
        #print('Check field has error')

    def is_element_present(self,element):
        try:
            expect(element).to_be_visible()
        except AssertionError:
            raise AssertionError(f'Element is not visible')