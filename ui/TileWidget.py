import kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ObjectProperty,ListProperty, BooleanProperty
from kivy.graphics import Color

class TileWidget(Widget):
    row = NumericProperty()
    col = NumericProperty()
    letter = StringProperty()
    game_engine = ObjectProperty()
    c = ListProperty()
    is_in_word = BooleanProperty()   
    

        