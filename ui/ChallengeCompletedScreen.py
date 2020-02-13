from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.metrics import *
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.clock import Clock
from kivy.animation import Animation

from ui.Sequence import Sequence
from ui.TileWidget import TileWidget

class ChallengeCompletedScreen(Screen):
    btn_continue = ObjectProperty()
    lbl_challenge_completed = ObjectProperty()
    lbl_level = ObjectProperty()
    lbl_challenge = ObjectProperty()

    @property
    def game_engine(self):
        return App.get_running_app().game_engine

    def __init__(self, **kwargs):
        super(ChallengeCompletedScreen, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter
        self.on_pre_enter = self.do_on_pre_enter
        #self.btn_continue.bind(on_touch_up = self.btn_continue_on_touch_up)

    def btn_continue_on_touch_up(self, instance, touch):
        if instance.collide_point(*touch.pos):
            App.get_running_app().status = "challenge_starting"
            self.manager.current = 'board'

    def do_on_pre_enter(self):
        self.lbl_challenge_completed.pos_hint = {"x":.0,"top":.84}
        self.lbl_challenge_completed.opacity = 0

        self.lbl_level.pos_hint = {"x":.05,"top":.75}      
        self.lbl_level.opacity = 0
        self.lbl_level.text = f"Level: {self.game_engine.level}"
        
        self.lbl_challenge.pos_hint = {"x":.1,"top":.70}
        self.lbl_challenge.text = f"Challenge: {self.game_engine.challenge}"
        self.lbl_challenge.opacity = 0
        
        self.btn_continue.pos_hint = {"x":.15,"center_y":.45}
        self.btn_continue.opacity = 0        

    def do_on_enter(self):    
        s = Sequence(Clock)

        a1 = Animation(opacity=1, pos_hint = {"x":.15,"top":.84}, d = 1, t = "in_out_quart")
        s.add_animation(a1, self.lbl_challenge_completed, 0.01)

        a2 = Animation(opacity=1, pos_hint = {"x":.15,"top":.75}, d = 1, t = "in_out_quart")
        s.add_animation(a2, self.lbl_level, 0.01)

        a3 = Animation(opacity=1, pos_hint = {"x":.15,"top":.70}, d = 1, t = "in_out_quart")
        s.add_animation(a3, self.lbl_challenge, 0.01)

        a4 = Animation(opacity=1, pos_hint = {"x":.15,"center_y":.5}, d = 1, t = "in_out_quart")
        s.add_animation(a4, self.btn_continue, 0.01)

        s.play()
