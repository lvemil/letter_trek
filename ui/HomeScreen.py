from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import ObjectProperty

from ui.TileWidget import TileWidget
from ui.StartButtonWidget import StartButtonWidget

class HomeScreen(Screen):
    gly_levels = ObjectProperty()
    scv_levels = ObjectProperty()
   
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.on_enter = self.do_on_pre_enter

    @property
    def game_engine(self):
        return App.get_running_app().game_engine

    def do_on_pre_enter(self):
        self.game_engine.load()
        self.current_level = self.game_engine.level if self.game_engine.get_level_progress() < 1 else self.game_engine.level + 1 
        progress = 1 #self.game_engine.get_level_progress()
        
        for i in range(1, self.game_engine.get_level_count()+1):
            l = StartButtonWidget()
            l.text = str(i)
            l.font_name = "fonts/zekton.ttf"
            l.font_size = dp(20)
            l.level = i
            if i > self.current_level:
                l.disabled = True
                l.progress = 1
            elif i < self.current_level:
                l.disabled = True
                #l.bind(on_touch_up = self.btn_start_on_touch_up)
                l.progress = 1    
            elif i == self.current_level:
                l.disabled = False
                l.bind(on_touch_up = self.btn_start_on_touch_up)
                l.progress = progress
                btn = l
            self.gly_levels.add_widget(l)
        
        self.scv_levels.scroll_to(btn, padding=dp(30))

    def btn_start_on_touch_up(self, instance, touch):
        if instance.collide_point(*touch.pos):
            #if instance.level < self.current_level:
            #    self.game_engine.level = instance.level
            #    self.game_engine.challenge = 0            
            self.manager.current = 'board'    
    
    