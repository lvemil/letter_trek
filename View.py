from Board import Board

class View:

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

    @challenge.setter
    def challenge(self, challenge):
        self.__challenge = challenge

    def refresh(self):
        pass