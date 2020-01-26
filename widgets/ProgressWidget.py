import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App

class ProgressWidget(Label):
    disabled = BooleanProperty()
    progress = NumericProperty()
    progress_start = NumericProperty()

    def __init__(self, **kwargs):
        super(ProgressWidget, self).__init__(**kwargs)