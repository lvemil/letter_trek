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
        
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.game_engine.touch(self.row, self.col)    
            print(f"{self.row} {self.col}")

    def letter_in_word(self):
        return self.letter in self.game_engine.current_word()

        