from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import *
from kivy.properties import StringProperty 
from kivy.app import App
from kivy.properties import ObjectProperty

from widgets.LetterScapeGameWidget import LetterScapeGameWidget
from widgets.TileWidget import TileWidget
from core.GameEngine import GameEngine

import random

class BoardScreen(Screen):
    game_widget: ObjectProperty()

    def __init__(self, **kwargs):
        super(BoardScreen, self).__init__(**kwargs)
        #self.on_enter = self.do_on_enter
        self.on_pre_enter = self.do_on_pre_enter

    def tile_on_touch_up(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.__game_engine.touch(instance.row, instance.col)    

    def do_on_pre_enter(self):
        
        if App.get_running_app().status == "starting": # initialize game board
            self.initialize_board()

        if App.get_running_app().status == "challenge_starting": # next challenge
            self.__game_engine.next_challenge()

        # update board
        self.set_level(self.__game_engine.level)
        self.set_challenge(self.__game_engine.challenge)
        self.set_word(self.__game_engine.word)
        self.add_tiles()

        # start clock
        self.__first_move = True
        self.game_widget.timer = 0
        self.__clock_event = Clock.schedule_interval(self.on_timer_interval, 1)

        # set app status
        App.get_running_app().status = "challenge_in_progress"

    def on_timer_interval(self, dt):
        if self.__first_move == False:
            self.game_widget.timer += 1
        return True

    def on_tile_move_completed(self, animation, widget):
        if self.__game_engine.check_challenge_completed():
            self.__clock_event.cancel()
            self.set_word("")
            self.clear_tiles()
 
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

        # update widget row and col
        tile.row = new_row
        tile.col = new_col

        # create animation
        anim = Animation(pos=(new_x, new_y), d = 0.1, t = "in_out_quart")
        anim.bind(on_complete = self.on_tile_move_completed)
        
        # run animation
        anim.start(tile)
        self.__first_move = False

    def on_tile_removed(self, animation, widget):
        self.game_widget.gly_tiles.remove_widget(widget)
        
        if len(self.get_all_tile_widgets()) == 0:
            App.get_running_app().status = "challenge_completed"
            self.manager.current = "challenge_completed"

    def add_tiles(self):
        self.game_widget.gly_tiles.clear_widgets()
        self.set_tiles_cols(self.__game_engine.board.cols)
        for r in range(self.__game_engine.board.rows):
            for c in range(self.__game_engine.board.cols):
                self.add_tile(self.__game_engine.board.get_tile(r, c), r, c)  

    def get_tile_widget(self, row, col):
        return [w for w in self.game_widget.gly_tiles.children if type(w) is TileWidget and w.row == row and w.col == col][0]

    def get_all_tile_widgets(self):
        return [w for w in self.game_widget.gly_tiles.children if type(w) is TileWidget]

    def set_level(self, level):
        self.game_widget.level = level

    def set_challenge(self, challenge):
        self.game_widget.challenge = challenge
        self.game_widget.level_challenges = self.__game_engine.level_challenges

    def set_word(self, word):
        self.game_widget.word = word

    def set_tiles_cols(self, cols):
        self.game_widget.gly_tiles.cols = cols

    def initialize_board(self):
        self.__game_engine = GameEngine()
        self.__game_engine.on_tile_moved += self.on_tile_moved
        self.__game_engine.start()

    def clear_tiles(self):
        # get all tile widgets
        all_tiles = self.get_all_tile_widgets()
        
        # animate
        for tile in all_tiles:
            d = random.choice([1,-1])
            new_center_x = tile.center_x + Window.size[0] * d
            anim = Animation(center_x=new_center_x, d = .2, t = "linear")
            anim.bind(on_complete = self.on_tile_removed)        
            anim.start(tile)

    def add_tile(self, letter, row, col):
        if letter == "_":
            self.game_widget.gly_tiles.add_widget(Label())
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
            t.bind(on_touch_up = self.tile_on_touch_up)

            self.game_widget.gly_tiles.add_widget(t)