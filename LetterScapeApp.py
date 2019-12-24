import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from widgets.LetterScapeGameWidget import LetterScapeGameWidget
from widgets.TileWidget import TileWidget

from core.GameEngine import GameEngine
from core.View import View

class LetterScapeApp(App):


    def build(self):
        rw = LetterScapeGameWidget()
        th = rw.children[0].children[0]

        self.__root_widget = rw
        self.__tiles_holder = th

        self.__game_engine = GameEngine(KivyView(self))
        self.__game_engine.start()

        #for _ in range(9):
        #    g.children[0].children[0].add_widget(Button())
        return  rw
        
    def set_level(self, level):
        self.__root_widget.level = level

    def set_challenge(self, challenge):
        self.__root_widget.challenge = challenge

    def set_word(self, word):
        self.__root_widget.word = word

    def clear_tiles(self):
        self.__tiles_holder.clear_widgets()

    def set_tiles_cols(self, cols):
        self.__tiles_holder.cols = cols

    def add_tile(self, letter, row, col):
        if letter == "_":
            self.__tiles_holder.add_widget(Label())
        else:
            t = TileWidget()
            t.letter = letter
            t.row = row
            t.col = col
            t.game_engine = self.__game_engine
            self.__tiles_holder.add_widget(t)

class KivyView(View):
    
    def __init__(self, app: LetterScapeApp):
        self.__app = app

    def refresh(self):
        self.__app.set_level(self.level)
        self.__app.set_challenge(self.challenge)
        self.__app.set_word(self.word)

        self.__app.clear_tiles()
        self.__app.set_tiles_cols(self.board.cols)
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                self.__app.add_tile(self.board.get_tile(r, c), r, c)
                