import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.app import App

class StartButtonWidget(Label):
    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
    
