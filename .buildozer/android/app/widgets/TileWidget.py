import kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ObjectProperty,ListProperty
from kivy.graphics import Color

class TileWidget(Widget):
    row = NumericProperty()
    col = NumericProperty()
    letter = StringProperty()
    game_engine = ObjectProperty()
    c = ListProperty()
    
    def letter_in_word(self):
        return self.letter in self.game_engine.current_word()

        