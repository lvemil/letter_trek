import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App

class StartButtonWidget(Label):
    disabled = BooleanProperty()
    progress = NumericProperty()

    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
    
