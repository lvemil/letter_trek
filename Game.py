from TerminalBoard import TerminalBoard
import pickle
import random

class Game:
    __level_def = {1:{"c":3, "bh":3, "bw":3, "wl":3}, 2:{"c":3, "bh":4, "bw":4, "wl":5},}

    def __init__(self):
        pass
 
    def start(self):
        self.__level = 0
        self.next_level()
 
    def next_level(self):
        self.__level += 1
        self.__challenge = 0
        self.next_challenge()

    def level_param(self, param_name):
        return self.__level_def[self.__level][param_name]

    def random_word(self, length):
        words = []
        with open('words.en.pkl','rb') as f:
            pickle.load(words, f)
        return random.choice([w for w in words if len(w) == length])

    def next_challenge(self):
        self.__board = TerminalBoard(self.level_param("bh"),self.level_param("bw"))
        self.__board.fill_random()
        self.__word = self.random_word(self.level_param)
        self.__board.set_word(self.__word)
        self.__board.show()

    def challenge_completed(self):
        print('done!!')
        if self.__challenge < self.level_param("c"):
            self.next_challenge()
        else:
            self.next_level()

    def touch(self, row, col):
        self.__board.touch(row, col)
        self.__board.show()
        if self.__board.solved(self.__word):
            self.challenge_completed()