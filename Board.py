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
        return row >= 0 and col >= 0 and row < self.__rows and col < self.__cols

    def inside_pos(self, pos):
        return pos >= 0 and pos < self.__rows * self.__cols

    def draw_tile(self, row, col):
        pass

    def fill_random(self):
        self.__tiles = ''
        for i in range(self.__rows * self.__cols):
            letter  = random.choice(self.__letters)
            self.__tiles += letter

    def fixed(self, r, c):
        return False

    def moved_position(self, r, c, d):
        dr = {0: -1, 1: 0, 2: 1, 3:  0}
        dc = {0:  0, 1: 1, 2: 0, 3: -1}
        return r + dr[d], c + dc[d]

    def set_word(self, word):
        # select start position
        r = random.choice(range(self.__rows))
        c = random.choice(range(self.__cols))
        while self.fixed(r, c):
            r = random.choice(range(self.__rows))
            c = random.choice(range(self.__cols))
        
        # determine word letter positions
        letter_positions = [(r,c)]
        for _ in range(len(word)-1):            
            while self.fixed(r, c) or (r,c) in letter_positions or not self.inside(r, c):
                d = random.choice(range(4))
                nr, nc = self.moved_position(r, c, d)
                if not self.fixed(nr, nc) and (nr, nc) not in letter_positions and self.inside(nr, nc):
                    r, c = nr, nc
            letter_positions.append((r,c))

        # set tiles
        for i in range(len(word)):
            self.set_tile(letter_positions[i][0],letter_positions[i][1], word[i])    
                
                

        
                
