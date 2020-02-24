import kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ObjectProperty,ListProperty, BooleanProperty
from kivy.graphics import Color
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.metrics import dp

class TileWidget(Label):
    row = NumericProperty()
    col = NumericProperty()
    letter = StringProperty()
    game_engine = ObjectProperty()
    is_in_word = BooleanProperty()   

    def shake(self):
        x = self.center_x
        nx = x + dp(5)
        Animation.stop_all(self)
        (
            Animation(
                center_x=nx,
                t='out_quad', d=.02
            ) + Animation(
                center_x=x,
                t='out_elastic', d=.5
            )
        ).start(self)
    

        