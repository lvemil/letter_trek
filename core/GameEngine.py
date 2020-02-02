from core.Board import Board
from core.Event import Event
from core.GameState import GameState

import pickle
import random

class GameEngine:
    __level_def = {
        1:{"c":5, "bh":3, "bw":3, "wl":2},
        2:{"c":3, "bh":3, "bw":3, "wl":3},
        3:{"c":3, "bh":3, "bw":3, "wl":4},
        4:{"c":3, "bh":4, "bw":4, "wl":5}, 
        5:{"c":3, "bh":4, "bw":4, "wl":5},
        6:{"c":2, "bh":3, "bw":3, "wl":2},
        7:{"c":3, "bh":3, "bw":3, "wl":3},
        8:{"c":3, "bh":3, "bw":3, "wl":4},
        9:{"c":3, "bh":4, "bw":4, "wl":5}, 
        10:{"c":30, "bh":3, "bw":3, "wl":3},
        11:{"c":2, "bh":3, "bw":3, "wl":2},
        12:{"c":3, "bh":3, "bw":3, "wl":3},
        13:{"c":3, "bh":3, "bw":3, "wl":4},
        14:{"c":3, "bh":4, "bw":4, "wl":5}, 
        15:{"c":3, "bh":4, "bw":4, "wl":5},
        16:{"c":2, "bh":3, "bw":3, "wl":2},
        17:{"c":3, "bh":3, "bw":3, "wl":3},
        18:{"c":3, "bh":3, "bw":3, "wl":4},
        19:{"c":3, "bh":4, "bw":4, "wl":5}, 
        20:{"c":3, "bh":4, "bw":4, "wl":5},
        21:{"c":2, "bh":3, "bw":3, "wl":2},
        22:{"c":3, "bh":3, "bw":3, "wl":3},
        23:{"c":3, "bh":3, "bw":3, "wl":4},
        24:{"c":3, "bh":4, "bw":4, "wl":5}, 
        25:{"c":3, "bh":4, "bw":4, "wl":5},
    }

    def __init__(self):
        self.on_board_reset = Event()
        self.on_tile_moved = Event()
        self.on_challenge_completed = Event()
        self.state = GameState()
 
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
    def level_challenges(self):
        return self.level_param("c")

    @property
    def challenge(self):
        return self.__challenge

    @challenge.setter
    def challenge(self, challenge):
        self.__challenge = challenge

    def start(self):
        self.__level = 0
        self.next_level()

    def load(self):
        self.state.load()
        self.level = self.state.level
        self.challenge = self.state.challenge
        
    def save(self):
        self.state.level = self.level
        self.state.challenge = self.challenge
        self.state.save()

    def get_level_count(self):
        return len(self.__level_def) - 1

    def get_level_progress(self):
        return self.challenge / self.level_param("c")

    def next_level(self):
        self.__level += 1
        self.__challenge = 0
        self.next_challenge()

    def level_param(self, param_name):
        return self.__level_def[self.__level][param_name]

    def random_word(self, word_len):
        with open('data/words_en.pkl','rb') as f:
            words = pickle.load(f)
            return random.choice([w for w in words if len(w) == word_len])

    def current_word(self):
        return self.__word 

    def set_board(self):
        self.__board = Board(self.level_param("bh"),self.level_param("bw"))
        self.__board.on_tile_moved += self.__on_board_tile_moved
        self.__board.fill_random()
        
        self.__word = self.random_word(self.level_param("wl"))
        
        self.__board.set_word(self.__word)
        
        self.__board.mess(self.__word)

        # fire on_board_changed event
        self.on_board_reset(self)

    def next_challenge(self):
        if self.__challenge >= self.level_param("c"):            
            self.__level += 1
            self.__challenge = 0
        
        self.__challenge += 1
        
        self.set_board()

    def check_challenge_completed(self):
        r = self.__board.solved(self.__word)
        if r == False:
            return False
        else:
            self.solution = r
            return True
        
    def touch(self, row, col):
        return self.__board.touch(row, col)

    def __on_board_tile_moved(self, sender, row, col, direction, new_row, new_col):
        self.on_tile_moved(self, row, col, direction, new_row, new_col)