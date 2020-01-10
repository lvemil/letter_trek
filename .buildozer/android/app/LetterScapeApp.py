import time

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from widgets.LetterScapeGameWidget import LetterScapeGameWidget
from widgets.TileWidget import TileWidget
from widgets.BoardScreen import BoardScreen
from widgets.HomeScreen import HomeScreen
from widgets.StartButtonWidget import StartButtonWidget

from core.GameEngine import GameEngine

class LetterScapeApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(BoardScreen(name='board'))

        return sm
    
    

