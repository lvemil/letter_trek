import random
from core.Event import Event

class Board:
    
    __letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, rows = 1, cols = 1):
        self.__rows = rows
        self.__cols = cols
        self.__tiles = "_" * (rows * cols)
        self.on_tile_moved = Event()
        
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

    def axis_to_pos(self, row, col):
        return row * (self.__cols) + col

    def pos_to_axis(self, pos):
        c = pos % self.__cols
        r = pos // self.__cols
        return r, c

    def get_tile(self, row, col):
        return self.__tiles[row][col]

    def set_tile(self, row, col, letter):
        #p = self.axis_to_pos(row, col)
        #self.__tiles = self.__tiles[:p] + letter + self.__tiles[p+1:]
        self.__tiles[row][col] = letter

    def get_tiles(self):
        return self.__tiles

    def get_tiles_str(self):
        flat = [item for sublist in self.__tiles for item in sublist]
        return "".join(flat)

    def set_tiles(self, tiles):
        if isinstance(tiles, str):
            l_tiles = [tiles[i : i + self.cols] for i in range(0, len(tiles), self.cols)]
            self.__tiles = [list(s) for s in l_tiles]
        else:
            self.__tiles = tiles.copy()
        
        #padding = self.__rows * self.__cols - len(tiles)
        #self.__tiles = self.__tiles + ("-" * padding) 

    def inside(self, row, col):
        return row >= 0 and col >= 0 and row < self.__rows and col < self.__cols

    def inside_pos(self, pos):
        return pos >= 0 and pos < self.__rows * self.__cols

    def draw_tile(self, row, col):
        pass

    def fill_random(self):
        tiles = ''
        for _ in range(self.__rows * self.__cols - 1):
            letter  = random.choice(self.__letters)
            tiles += letter
        tiles += "_"
        self.set_tiles(tiles)

    def fixed(self, r, c):
        return False

    def empty(self, r, c):
        return self.get_tile(r, c) == '_'

    def adjacent_position(self, r, c, d):
        dr = {0: -1, 1: 0, 2: 1, 3:  0}
        dc = {0:  0, 1: 1, 2: 0, 3: -1}
        return r + dr[d], c + dc[d]

    def get_random_postion(self):
        r = random.choice(range(self.__rows))
        c = random.choice(range(self.__cols))
        return r, c

    def set_word(self, word):
        positions_r_c = [self.pos_to_axis(i) for i in range(self.rows*self.cols)]
        tile_positions = [(r,c) 
            for (r,c) in positions_r_c
            if self.fixed(r,c) == False 
                and self.empty(r,c) == False]
        random_positions = random.sample(tile_positions, k=len(word))
        for i in range(len(word)):
            r,c = random_positions[i]
            self.set_tile(r, c, word[i])
 
    def solved_at(self, word, row, col, depth = 0):
        self.__path.append((row,col))
        
        adjacent_rc = [self.adjacent_position(row, col, d) for d in [0, 1, 2, 3]]
        adjacent_rc_inside = [(r,c) for (r,c) in adjacent_rc if self.inside(r,c) and (r,c) not in self.__path]
        neighbors= [self.get_tile(r,c) for r,c in adjacent_rc_inside]
        
        tile = word[depth + 1]
        good_neighbors_idx = [i for i,o in enumerate(neighbors) if o == tile]

        if depth + 1 == len(word) - 1:
            if len(good_neighbors_idx) > 0:
                self.__path.append(adjacent_rc_inside[0])
                return True
            else:
                return False

        for i in good_neighbors_idx:
            nr, nc = adjacent_rc_inside[i]
            res = self.solved_at(word, nr, nc, depth + 1)
            if res == True:
                return True
            else:
                self.__path.pop()

        return False

    def solved(self, word):
        # get postions of first letter
        flat = [item for sublist in self.__tiles for item in sublist]
        lp = [self.pos_to_axis(p) for p, char in enumerate(flat) if char == word[0]]
        
        # check solved in every found position
        self.__path = []
        for r,c in lp:
            if self.solved_at(word, r, c, 0):
                return self.__path
        
        return False
    
    def swap_tiles(self, row, col, new_row, new_col):
        t = self.get_tile(row, col)
        self.set_tile(row, col, self.get_tile(new_row, new_col))
        self.set_tile(new_row, new_col, t)

    def __mess(self):
        l = [c for c in self.get_tiles_str()]
        random.shuffle(l)
        self.set_tiles("".join(l))

    def mess(self, word):
        self.__mess()
        while self.solved(word):
            self.__mess()

    def touch_d(self, row, col, d):
        r, c = self.adjacent_position(row, col, d)
        pos_list = [(row, col)]
        while r >= 0 and c >= 0 and r < self.__rows and c < self.__cols:
            pos_list.append((r, c))
            if self.get_tile(r, c) == '_':
                for i in range(len(pos_list) - 1, 0, -1):
                    r1, c1 = pos_list[i]
                    r2, c2 = pos_list[i-1]
                    self.swap_tiles(r1,c1, r2, c2)
                    self.on_tile_moved(self, r2,c2, d, r1, c1)
                return True
            r, c = self.adjacent_position(r, c, d)

    def touch(self, row, col):
        for d in [0,1,2,3]:
            r, c = self.adjacent_position(row, col, d)
            pos_list = [(row, col)]
            while r >= 0 and c >= 0 and r < self.__rows and c < self.__cols:
                pos_list.append((r, c))
                if self.get_tile(r, c) == '_':
                    for i in range(len(pos_list) - 1, 0, -1):
                        r1, c1 = pos_list[i]
                        r2, c2 = pos_list[i-1]
                        self.swap_tiles(r1,c1, r2, c2)
                        self.on_tile_moved(self, r2,c2, d, r1, c1)
                    return True
                r, c = self.adjacent_position(r, c, d)
        return False

    def get_empty_pos(self):
        flat = [item for sublist in self.__tiles for item in sublist]
        return self.pos_to_axis(flat.index('_'))

    def copy(self):
        b = Board(rows = self.__rows, cols = self.__cols)
        b.set_tiles(self.get_tiles())
        return b

    







        
                
