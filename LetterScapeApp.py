import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color

from widgets.LetterScapeGameWidget import LetterScapeGameWidget
from widgets.TileWidget import TileWidget

from core.GameEngine import GameEngine

class LetterScapeApp(App):


    def build(self):
        rw = LetterScapeGameWidget()
        th = rw.children[0].children[0]

        self.__root_widget = rw
        self.__tiles_holder = th

        self.__game_engine = GameEngine()

        self.__game_engine.on_board_reset += self.on_board_reset

        self.__game_engine.start()

        return  rw
    
    def on_board_reset(self, sender, earg):
        self.set_level(sender.level)
        self.set_challenge(sender.challenge)
        self.set_word(sender.word)

        self.clear_tiles()
        self.set_tiles_cols(sender.board.cols)
        for r in range(sender.board.rows):
            for c in range(sender.board.cols):
                self.add_tile(sender.board.get_tile(r, c), r, c)        

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
            t.c = [0,1,1,.9] if t.letter_in_word() else [1,1,1,.9]
            self.__tiles_holder.add_widget(t)

