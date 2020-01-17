import kivy
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

class LetterScapeGameWidget(Widget):
    level = NumericProperty()
    challenge = NumericProperty()
    level_challenges = NumericProperty()
    word = StringProperty()
    timer = NumericProperty()
    gly_tiles = ObjectProperty()