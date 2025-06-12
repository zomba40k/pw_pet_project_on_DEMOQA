from pages.Forms.practice_form_page import PracticeFormPage
import pytest


link = 'https://demoqa.com/automation-practice-form'
class TestPracticeFormPage:

    def test_form_valid(self,page):
        form = PracticeFormPage(page)
        form.open(link)
        form.fill_fields()
        first_name = form.fill_first_name()
        last_name = form.fill_last_name()
        email = form.fill_email()
        address = form.fill_address()
        phone = form.fill_phone()
        gender = form.select_gender()
        date_data = form.select_date()
        subject = form.select_subject()
        hobbies = form.select_hobby()
        picture = form.upload()
        state = form.select_state()
        city = form.select_city()
        form.click(form.submit_btn)
        form.verify_modal_data({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'gender': gender,
            'date': date_data,
            'subject': subject,
            'hobbies': hobbies,
            'picture': picture,
            'address': address,
            'state': state,
            'city': city
        })
        form.modal_close_btn.click()
        form.page.wait_for_timeout(200)
        assert not form.is_modal_visible(), 'Модальное окно не закрылось'


    @pytest.mark.parametrize(
        "invalid_data, error_field",
        [
            ({"first_name": ""}, "first_name"),
            ({"last_name": ""}, "last_name"),
            ({"phone": "123abc"}, "phone"),
            ({"gender": None}, "gender"),
        ]
    )
    def test_invalid_field(self,page, invalid_data, error_field):
        form = PracticeFormPage(page)
        form.open(link)

        field = form.fill_form_invalid(invalid_data, error_field=error_field)
        form.submit_btn.click()

        form.check_field_has_error(field)

        assert not form.is_modal_visible(), 'Модальное окно с данными появилось, хотя поля не прошли валидацию'

