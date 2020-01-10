from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import *

from widgets.LetterScapeGameWidget import LetterScapeGameWidget
from widgets.TileWidget import TileWidget
from core.GameEngine import GameEngine

class BoardScreen(Screen):
    
    def __init__(self, **kwargs):
        super(BoardScreen, self).__init__(**kwargs)
        self.on_enter = self.do_on_enter

    def do_on_enter(self):
        rw = LetterScapeGameWidget()

        self.add_widget(rw)

        th = rw.children[0].children[1]

        self.__root_widget = rw
        self.__tiles_holder = th

        self.__game_engine = GameEngine()

        self.__game_engine.on_board_reset += self.on_board_reset
        self.__game_engine.on_tile_moved += self.on_tile_moved

        Clock.schedule_interval(self.timer_interval, 1)

        self.__game_engine.start()

    def timer_interval(self, dt):
        if self.__first_move == False:
            self.__root_widget.timer += 1
        return True

    def add_tiles(self):
        self.__tiles_holder.clear_widgets()
        self.set_tiles_cols(self.__game_engine.board.cols)
        for r in range(self.__game_engine.board.rows):
            for c in range(self.__game_engine.board.cols):
                self.add_tile(self.__game_engine.board.get_tile(r, c), r, c)  

    def on_board_reset(self, sender):
        self.set_level(sender.level)
        self.set_challenge(sender.challenge)
        self.set_word(sender.word)
        self.__root_widget.timer = 0
        
        if len(self.get_all_tile_widgets()) > 0:
            self.clear_tiles()
        else:
            self.add_tiles()

        self.__first_move = True

    def on_tile_moved(self, sender, row, col, direction, new_row, new_col):
        # get touched tile widget
        tile = self.get_tile_widget(row, col)

        # calculate new position    
        if direction == 0: # up
            new_x = tile.x 
            new_y = tile.y + tile.height + 10
        elif direction == 1: # rigth
            new_x = tile.x + tile.width + 10
            new_y = tile.y
        elif direction == 2: # down
            new_x = tile.x 
            new_y = tile.y - tile.height - 10
        elif direction == 3: # left
            new_x = tile.x - tile.width - 10
            new_y = tile.y

        print(f"tile in {row}, {col} moved to {direction} ({tile.x},{tile.y})->({new_x},{new_y})")

        # update widget row and col
        tile.row = new_row
        tile.col = new_col

        # create animation
        anim = Animation(pos=(new_x, new_y), d = 0.1, t = "in_out_quart")
        
        # run animation
        anim.start(tile)

        self.__first_move = False

    def get_tile_widget(self, row, col):
        tile = [w for w in self.__tiles_holder.children if type(w) is TileWidget and w.row == row and w.col == col][0]
        return tile

    def get_all_tile_widgets(self):
        return [w for w in self.__tiles_holder.children if type(w) is TileWidget]

    def set_level(self, level):
        self.__root_widget.level = level

    def set_challenge(self, challenge):
        self.__root_widget.challenge = challenge
        self.__root_widget.level_challenges = self.__game_engine.level_challenges

    def set_word(self, word):
        self.__root_widget.word = word

    def remove_tile_widget(self, animation, widget):
        self.__tiles_holder.remove_widget(widget)
        if len(self.get_all_tile_widgets()) == 0:
            self.add_tiles()

    def clear_tiles(self):
        # get all tile widgets
        all_tiles = self.get_all_tile_widgets()
        # animate
        anim = Animation(opacity=0, d = 0.5, t = "linear")
        anim.bind(on_complete = self.remove_tile_widget)
        for tile in all_tiles:
            anim.start(tile)

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
            t.c = [0.973, 0.463, 0.160, 1] if t.letter_in_word() else [0.176, 0.804, 0.796, 1]
            t.font_name = "fonts/zekton.ttf"
            win_w = Window.size[0] - (dp(10) * 2)
            t.size_hint_y = None
            t.height = win_w / self.__game_engine.board.rows

            self.__tiles_holder.add_widget(t)