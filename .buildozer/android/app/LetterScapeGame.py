import kivy
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty 

class LetterScapeGame(Widget):
    level = NumericProperty()
    challenge = NumericProperty()
    word = StringProperty()