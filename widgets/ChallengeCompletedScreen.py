from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import *
from kivy.properties import ObjectProperty
from kivy.app import App

from widgets.TileWidget import TileWidget


class ChallengeCompletedScreen(Screen):
    btn_continue = ObjectProperty()

    def __init__(self, **kwargs):
        super(ChallengeCompletedScreen, self).__init__(**kwargs)
        self.btn_continue.bind(on_touch_up = self.btn_continue_on_touch_up)

    def btn_continue_on_touch_up(self, instance, touch):
        if self.collide_point(*touch.pos):
            if App.get_running_app().status == "challenge_completed":
                App.get_running_app().status = "challenge_starting"
            
            self.manager.current = 'board'
