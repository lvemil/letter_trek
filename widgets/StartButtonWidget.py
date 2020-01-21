import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.app import App

class StartButtonWidget(Label):
    disabled = BooleanProperty()

    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
    
