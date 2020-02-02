from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import *
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.animation import Animation

from widgets.animations.Single import Single
from widgets.animations.Parallel import Parallel
from widgets.animations.Serie import Serie
from widgets.TileWidget import TileWidget

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

    def btn_continue_on_touch_up(self, instance, touch):
        if self.collide_point(*touch.pos):
            if App.get_running_app().status == "challenge_completed":
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

    def do_on_animation_complete(self, *args):
        print("done!")

    def do_on_enter(self):
        
        a1 = Animation(opacity=1, pos_hint = {"x":.15,"top":.84}, d = 1, t = "in_out_quart")
        s1 = Single(a1, self.lbl_challenge_completed)  
        #anim.start(self.lbl_challenge_completed)
        
        a2 = Animation(opacity=1, pos_hint = {"x":.15,"top":.75}, d = 1, t = "in_out_quart")
        s2 = Single(a2, self.lbl_level) 
        #anim.start(self.lbl_level)

        a3 = Animation(opacity=1, pos_hint = {"x":.15,"top":.70}, d = 1, t = "in_out_quart")
        s3 = Single(a3, self.lbl_challenge)
        #anim.start(self.lbl_challenge)

        a4 = Animation(opacity=1, pos_hint = {"x":.15,"center_y":.5}, d = 1, t = "in_out_quart")
        s4 = Single(a4, self.btn_continue)
        #anim.start(self.btn_continue)

        p = Parallel()
        p.add_child(s1)
        p.add_child(s2)
        p.add_child(s3)
        
        s = Serie()
        s.add_child(p)
        s.add_child(s4)
        s.on_complete += self.do_on_animation_complete

        s.play()
