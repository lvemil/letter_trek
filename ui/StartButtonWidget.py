import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior

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
    
