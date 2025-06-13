from pages.base_page import BasePage


class SliderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.slider = self.page.locator("input[type='range']")
        self.output = self.page.locator('#sliderValue')


    def get_value(self) -> int:
        return int(self.output.input_value())

    def set_slider_by_drag(self,value:str = 'max'):
        """По причине невозможности расположения слайдера на конкретном значении на разных экранах,
         вынужден проверять возможность установки значения либо max, либо min"""
        box = self.slider.bounding_box()
        x_center = box['x']+box['width']/2
        y_center = box['y']+box['height']/2

        self.page.mouse.move(x_center,y_center )
        self.page.mouse.down()
        if value == 'max':
            self.page.mouse.move(x_center+box['width'], y_center,steps=10)
        else:
            self.page.mouse.move(x_center - box['width'], y_center, steps=10)

        self.page.mouse.up()

    def set_slider_by_arrows(self,steps:int=10,isVertical :bool=False):
        self.slider.focus()
        if isVertical:
            key = 'ArrowUp' if steps>0 else 'ArrowDown'
        else:
            key = 'ArrowRight' if steps>0 else 'ArrowLeft'
        for i in range(abs(steps)):
            self.page.keyboard.press(key)

