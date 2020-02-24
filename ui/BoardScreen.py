from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.app import App

from ui.TileWidget import TileWidget
from ui.ProgressWidget import ProgressWidget
from ui.Sequence import Sequence

from core.GameEngine import GameEngine

import random

class BoardScreen(Screen):
    level = NumericProperty()
    challenge = NumericProperty()
    level_challenges = NumericProperty()
    word = StringProperty()
    timer = NumericProperty()

    gly_tiles = ObjectProperty()
    pro_challenge = ObjectProperty()
    #pro_timer = ObjectProperty()
    pro_level = ObjectProperty()
    pro_moves = ObjectProperty()
    btn_restart = ObjectProperty()
    btn_back = ObjectProperty()

    @property
    def game_engine(self):
        return App.get_running_app().game_engine

    def __init__(self, **kwargs):
        super(BoardScreen, self).__init__(**kwargs)
        #self.on_enter = self.do_on_enter
        self.on_pre_enter = self.do_on_pre_enter
        self.on_enter = self.do_on_enter
        self.game_engine.on_tile_moved += self.on_tile_moved

    def btn_back_on_release(self, instance):
        self.manager.current = "home" 

    def btn_restart_on_release(self, instance): #, touch):        
        # stop pro_moves blinking
        if self.available_moves == 0:
            self.blink_moves.cancel_all(self.pro_moves, "opacity")
            self.pro_moves.opacity = 1
            self.pro_moves.accent = False
        
        # reset board
        self.game_engine.board.set_tiles(self.starting_tiles)
        self.add_tiles(self.game_engine.board.get_tiles())
        
        # reset availables moves
        self.available_moves = self.max_moves
        self.pro_moves.text = str(self.available_moves) 
        self.pro_moves.progress = 1

        # move tiles outside
        print("restart - move outside" )
        Clock.schedule_once(self.clear_all_tiles, .01)
        Clock.schedule_once(self.animate_tiles_in, .21)
        
    def animate_tiles_in(self, *args):
        for tile in self.get_all_tile_widgets():
            new_x = self.__tiles_x[f"{tile.row}_{tile.col}"]
            anim = Animation(x=new_x, d = .2, t = "linear")
            anim.start(tile)

    def do_on_enter(self):
        # animate tiles in
        self.animate_tiles_in()

    def tile_on_touch_up(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if self.available_moves > 0 and self.game_engine.touch(instance.row, instance.col):
                # update available moves
                self.available_moves -= 1
                self.pro_moves.text = str(self.available_moves) 
                self.pro_moves.progress = self.available_moves / self.max_moves 
                if self.available_moves == 0 and not self.game_engine.check_challenge_completed():     
                    self.pro_moves.accent = True                   
                    fade = Animation(opacity = 0, d = .25, t = "linear")   
                    show = Animation(opacity = 1, d = .25, t = "linear")    
                    self.blink_moves = fade + show
                    self.blink_moves.repeat = True
                    self.blink_moves.start(self.pro_moves)
            else:
                x = instance.center_x
                nx = x + dp(5)
                Animation.stop_all(instance)
                (
                    Animation(
                        center_x=nx,
                        t='out_quad', d=.02
                    ) + Animation(
                        center_x=x,
                        t='out_elastic', d=.5
                    )
                ).start(instance)

    def move_tiles_outside(self, dt):
        print("move outside")
        # record tiles position
        self.__tiles_x = dict([(f"{t.row}_{t.col}",t.x) for t in self.get_all_tile_widgets()])
        
        # move tiles outside
        for tile in self.get_all_tile_widgets():
            d = random.choice([1,-1])
            tile.pos = (tile.x + Window.size[0] * d, tile.y )       

    def do_on_pre_enter(self):
        self.game_engine.next_challenge()
        self.starting_tiles = self.game_engine.board.get_tiles()            

        # update board
        self.set_level(self.game_engine.level)
        self.set_challenge(self.game_engine.challenge)
        self.set_word(self.game_engine.word)
        self.add_tiles(self.game_engine.board.get_tiles())
        
        # available moves
        self.max_moves = self.game_engine.board.solve(self.game_engine.word)
        self.available_moves = self.max_moves
        self.pro_moves.text = str(self.available_moves) 
        self.pro_moves.progress = 1

        Clock.schedule_once(self.move_tiles_outside, .01)
        
        # start clock
        #self.__first_move = True
        #self.timer = 0
        #self.pro_timer.text = "0"
        #self.__clock_event = Clock.schedule_interval(self.on_timer_interval, 1)

        # set app status
        App.get_running_app().status = "challenge_in_progress"

    """ def on_timer_interval(self, dt):
        if self.__first_move == False:
            self.timer += 1
            self.pro_timer.progress = ((30 * (self.timer % 12)) + 30) / 360
            self.pro_timer.progress_start = (30 * (self.timer % 12)) / 360
            self.pro_timer.text = str(self.timer)
        return True """

    def on_tile_move_completed(self, animation, widget):
        if self.game_engine.check_challenge_completed():
            #self.__clock_event.cancel()
            self.game_engine.save()
            self.set_word("")
            self.clear_tiles()
 
    def on_tile_moved(self, sender, row, col, direction, new_row, new_col):
        # get touched tile widget
        tile = self.get_tile_widget(row, col)
        padding = dp(5)
        # calculate new position    
        if direction == 0: # up
            new_x = tile.x 
            new_y = tile.y + tile.height + padding
        elif direction == 1: # rigth
            new_x = tile.x + tile.width + padding
            new_y = tile.y
        elif direction == 2: # down
            new_x = tile.x 
            new_y = tile.y - tile.height - padding
        elif direction == 3: # left
            new_x = tile.x - tile.width - padding
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

    def on_all_tiles_removed(self, dt):
        App.get_running_app().status = "challenge_completed"
        self.manager.current = "challenge_completed"  

    """ def add_tiles(self):
        self.gly_tiles.clear_widgets()
        self.set_tiles_cols(self.game_engine.board.cols)
        for r in range(self.game_engine.board.rows):
            for c in range(self.game_engine.board.cols):
                self.add_tile(self.game_engine.board.get_tile(r, c), r, c)   """

    def add_tiles(self, tiles):
        self.gly_tiles.clear_widgets()
        self.set_tiles_cols(self.game_engine.board.cols)
        p = 0
        for r in range(self.game_engine.board.rows):
            for c in range(self.game_engine.board.cols):
                self.add_tile(tiles[p], r, c)  
                p += 1

    def get_tile_widget(self, row, col):
        return [w for w in self.gly_tiles.children if type(w) is TileWidget and w.row == row and w.col == col][0]

    def get_all_tile_widgets(self, exclude=[]):
        return [w for w in self.gly_tiles.children if (type(w) is TileWidget) and ((w.row, w.col) not in exclude)]

    def set_level(self, level):
        self.level = level
        #self.pro_level.text = str(level)
        #self.pro_level.progress = level / self.game_engine.get_level_count()

    def set_challenge(self, challenge):
        self.challenge = challenge
        self.level_challenges = self.game_engine.level_challenges
        #self.pro_challenge.progress = ((challenge-1) / (self.game_engine.level_challenges if self.game_engine.level_challenges > 0 else 1))
        #self.pro_challenge.text = str(challenge)

    def set_word(self, word):
        self.word = word

    def set_tiles_cols(self, cols):
        self.gly_tiles.cols = cols

    def initialize_board(self):
        self.game_engine.next_challenge()

    def clear_all_tiles(self, *args):
        tiles = self.get_all_tile_widgets()
        
        s = Sequence(Clock)

        for tile in tiles:
            d = random.choice([1,-1])
            new_center_x = tile.center_x + Window.size[0] * d
            anim = Animation(center_x=new_center_x, d = .2, t = "linear")
            s.add_animation(anim, tile, 0.01)

        s.play()

    def clear_tiles(self):
        solution_tiles = [w     
            for w in self.gly_tiles.children 
            if (type(w) is TileWidget) 
                and ((w.row, w.col) in self.game_engine.solution)]
        not_solution_tiles = [w 
            for w in self.gly_tiles.children 
            if (type(w) is TileWidget) 
                and ((w.row, w.col) not in self.game_engine.solution)]
        
        s = Sequence(Clock)

        for tile in not_solution_tiles:
            d = random.choice([1,-1])
            new_center_x = tile.center_x + Window.size[0] * d
            anim = Animation(center_x=new_center_x, d = .2, t = "linear")
            s.add_animation(anim, tile, 0.01)

        for tile in solution_tiles:
            d = random.choice([1,-1])
            new_center_x = tile.center_x + Window.size[0] * d
            anim = Animation(center_x=new_center_x, d = .2, t = "linear")
            s.add_animation(anim, tile, 0.5)
        
        s.play()

        Clock.schedule_once(self.on_all_tiles_removed, 1)

    def add_tile(self, letter, row, col):
        if letter == "_":
            self.gly_tiles.add_widget(Label())
        else:
            t = TileWidget()
            t.letter = letter
            t.row = row
            t.col = col
            t.game_engine = self.game_engine
            t.is_in_word = letter in self.game_engine.current_word()
            win_w = Window.size[0] - (dp(10) * 2)
            #t.size_hint_y = None
            #t.height = win_w / self.game_engine.board.rows
            t.bind(on_touch_down = self.tile_on_touch_up)
            
            self.gly_tiles.add_widget(t)