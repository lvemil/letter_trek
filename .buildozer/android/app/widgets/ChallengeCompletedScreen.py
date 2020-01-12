from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import *

from widgets.TileWidget import TileWidget


class ChallengeCompletedScreen(Screen):
    def __init__(self, **kwargs):
        super(ChallengeCompletedScreen, self).__init__(**kwargs)