import random

class Board:
    
    __letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, rows = 1, cols = 1):
        self.__rows = rows
        self.__cols = cols
        self.__tiles = "-" * (rows * cols)
        
    @property
    def rows(self):
        return self.__rows
    
    @rows.setter
    def rows(self, rows):
        self.__rows = rows

    @property
    def cols(self):
        return self.__cols
    
    @cols.setter
    def cols(self, cols):
        self.__cols = cols

    def calculate_position(self, row, col):
        assert self.inside(row, col)
        return row * (self.__cols) + col

    def get_tile(self, row, col):
        assert self.inside(row, col)
        return self.__tiles[self.calculate_position(row, col)]

    def set_tile(self, row, col, letter):
        assert self.inside(row, col)
        p = self.calculate_position(row, col)
        self.__tiles = self.__tiles[:p] + letter + self.__tiles[p+1:]

    def get_tiles(self):
        return self.__tiles

    def set_tiles(self, tiles):
        self.__tiles = tiles
        padding = self.__rows * self.__cols - len(tiles)
        self.__tiles = self.__tiles + ("-" * padding) 

    def show(self):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.draw_tile(r, c)
            print("")

    def inside(self, row, col):
        return row < self.__rows and col < self.__cols

    def draw_tile(self, row, col):
        pass

    def fill_random(self):
        self.__tiles = ''
        for i in range(self.__rows * self.__cols):
            letter  = random.choice(self.__letters)
            self.__tiles += letter
