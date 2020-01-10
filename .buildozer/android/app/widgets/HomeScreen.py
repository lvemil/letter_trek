from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import *

from widgets.TileWidget import TileWidget


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
    
    