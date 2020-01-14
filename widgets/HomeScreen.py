from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ObjectProperty

from widgets.TileWidget import TileWidget

class HomeScreen(Screen):
    btn_start = ObjectProperty()

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.btn_start.bind(on_touch_up = self.btn_start_on_touch_up)

    def btn_start_on_touch_up(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.manager.current = 'board'    
    
    