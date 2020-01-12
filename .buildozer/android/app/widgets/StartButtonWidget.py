import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.app import App

class StartButtonWidget(Label):
    def __init__(self, **kwargs):
        super(StartButtonWidget, self).__init__(**kwargs)
        
    screen = ObjectProperty()

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if App.get_running_app().status == "challenge_completed":
                App.get_running_app().status = "challenge_starting"
            
            self.screen.manager.current = 'board'    
