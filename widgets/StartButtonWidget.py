import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class StartButtonWidget(Label):
    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
        
    screen = ObjectProperty()

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.screen.manager.current = 'board'    
