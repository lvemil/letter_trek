from core.Board import Board
from core.Event import Event
import pickle
import random

class GameEngine:
    __level_def = {
        1:{"c":3, "bh":3, "bw":3, "wl":2},
        2:{"c":3, "bh":3, "bw":3, "wl":3},
        3:{"c":3, "bh":3, "bw":3, "wl":4}, 
        4:{"c":3, "bh":4, "bw":4, "wl":5}
    }

    def __init__(self):
        self.on_board_reset = Event()
        self.on_tile_moved = Event()
 
    @property
    def board(self):
        return self.__board
    
    @board.setter
    def board(self, board):
        self.__board = board

    @property
    def word(self):
        return self.__word
    
    @word.setter
    def word(self, word):
        self.__word = word

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def challenge(self):
        return self.__challenge

    @challenge.setter
    def challenge(self, challenge):
        self.__challenge = challenge

    def start(self):
        self.__level = 0
        self.next_level()
 
    def next_level(self):
        self.__level += 1
        self.__challenge = 0
        self.next_challenge()

    def level_param(self, param_name):
        return self.__level_def[self.__level][param_name]

    def random_word(self, word_len):
        with open('words_en.pkl','rb') as f:
            words = pickle.load(f)
            return random.choice([w for w in words if len(w) == word_len])

    def current_word(self):
        return self.__word 


    def next_challenge(self):
        self.__challenge += 1
        
        self.__board = Board(self.level_param("bh"),self.level_param("bw"))
        self.__board.on_tile_moved += self.__on_board_tile_moved
        self.__board.fill_random()
        
        self.__word = self.random_word(self.level_param("wl"))
        
        self.__board.set_word(self.__word)
        
        self.__board.mess(self.__word)

        # fire on_board_changed event
        self.on_board_reset(self)

        # refresh view
        #self.__view.word = self.__word
        #self.__view.board = self.__board
        #self.__view.challenge = self.__challenge
        #self.__view.level = self.__level
        #self.__view.refresh()

    def challenge_completed(self):
        if self.__challenge < self.level_param("c"):
            self.next_challenge()
        else:
            self.next_level()

    def touch(self, row, col):
        tile_moved = self.__board.touch(row, col)
        #self.on_board_reset(self)

        if tile_moved and self.__board.solved(self.__word):            
            self.challenge_completed()

    def __on_board_tile_moved(self, sender, row, col, direction, new_row, new_col):
        self.on_tile_moved(self, row, col, direction, new_row, new_col)