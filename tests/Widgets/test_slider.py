from pages.Widgets.slider_page import SliderPage
import pytest

link = 'https://demoqa.com/slider'
@pytest.mark.Widgets
class TestSliderPage:
    @pytest.mark.parametrize('value',['max','min'])
    def test_slide_by_drag(self,page,value):
        slider = SliderPage(page)
        slider.open(link)
        slider.set_slider_by_drag(value)
        new = slider.get_value()
        if value == 'max':
            assert new == 100, f'Слайдер не сдвинулся на необходимое значение, ожидалось 100, получил {new}'
        else:
           assert new==0, f'Слайдер не сдвинулся на необходимое значение, ожидалось 0, получил {new}'

    @pytest.mark.parametrize(
        ("value", "is_vertical"),
        [
            (10, True),  # вертикально
            (-10, False),  # горизонтально
            (-10, True),  # вертикально
            (10, False),  # горизонтально
        ]
    )
    def test_slide_by_arrows(self,page,value,is_vertical):
        slider = SliderPage(page)
        slider.open(link)
        inital = slider.get_value()
        slider.set_slider_by_arrows(value,is_vertical)
        new = slider.get_value()

        assert new == inital+value, f'Слайдер не сдвинулся на необходимое значение, ожидалось {inital+value}, получил {new}'