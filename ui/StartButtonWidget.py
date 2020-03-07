import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation

class StartButtonWidget(ButtonBehavior, Label):
    disabled = BooleanProperty()
    progress = NumericProperty()
    pressed = BooleanProperty()

    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
        self.pressed = False

    def on_press(self):
        self.pressed = True
        print('pressed')

    def on_release(self):
        self.pressed = False
    
    def grow(self):
        Animation.stop_all(self)
        
        a = (
            Animation(scale_x=1.2, scale_y=1.2, t='out_quad', d=.03*5) +
            Animation(scale_x=1, scale_y=1, t='out_elastic', d=.4*5)
        )
        a.repeat = True
        a.start(self)
