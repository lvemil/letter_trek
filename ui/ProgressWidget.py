import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty
from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock

class ProgressWidget(Label):
    disabled = BooleanProperty()
    progress = NumericProperty()
    progress_start = NumericProperty()
    accent = BooleanProperty()

    def __init__(self, **kwargs):
        super(ProgressWidget, self).__init__(**kwargs)
        self.disabled = False
        self.accent = False 

    def blink(self):
        fade = Animation(opacity = 0, d = .25, t = "linear")   
        show = Animation(opacity = 1, d = .25, t = "linear")    
        blink_moves = fade + show
        blink_moves.repeat = True
        blink_moves.start(self)  

    def show(self, *args):
        print(self)
        self.opacity = 1.0
        
    def stop_blink(self):
        Animation.stop_all(self)
        Clock.schedule_once(self.show, 0.5)