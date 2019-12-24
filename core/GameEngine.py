from core.Board import Board
import pickle
import random

class GameEngine:
    __level_def = {1:{"c":3, "bh":3, "bw":3, "wl":3}, 2:{"c":3, "bh":4, "bw":4, "wl":5},}

    def __init__(self, view):
        self.__view = view
 
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
        self.__board.fill_random()
        self.__word = self.random_word(self.level_param("wl"))
        self.__board.set_word(self.__word)
        #self.__board.mess(4, self.__word)
        self.__board.mess()

        # refresh view
        self.__view.word = self.__word
        self.__view.board = self.__board
        self.__view.challenge = self.__challenge
        self.__view.level = self.__level
        self.__view.refresh()

    def challenge_completed(self):
        if self.__challenge < self.level_param("c"):
            self.next_challenge()
        else:
            self.next_level()

    def touch(self, row, col):
        self.__board.touch(row, col)
        self.__view.refresh()
        if self.__board.solved(self.__word):
            self.challenge_completed()