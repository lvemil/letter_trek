from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import ObjectProperty

from widgets.TileWidget import TileWidget
from widgets.StartButtonWidget import StartButtonWidget

class HomeScreen(Screen):
    #btn_start = ObjectProperty()
    gly_levels = ObjectProperty()

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.on_enter = self.do_on_pre_enter
        
    def do_on_pre_enter(self):

        App.get_running_app().game_state.load()
        App.get_running_app().game_state.level = 2

        for i in range(1, App.get_running_app().game_engine.get_level_count()+1):
            l = StartButtonWidget()
            l.text = str(i)
            l.font_name = "fonts/zekton.ttf"
            l.font_size = dp(20)
            l.disabled = True if i > App.get_running_app().game_state.level  else False
            if l.disabled == False:
                l.bind(on_touch_up = self.btn_start_on_touch_up)
            self.gly_levels.add_widget(l)

    def btn_start_on_touch_up(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'board'    
    
    