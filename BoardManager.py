class BoardManager:
    
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
        return row * (self.__cols) + (col + 1)

    def get_tile(self, row, col):
        if self.__rows < row or self.__cols < col:
            return None
        return self.__tiles[self.calculate_position(row, col)]

    def set_tile(self, row, col, letter):
        if self.__rows < row or self.__cols < col:
            return
        p = self.calculate_position(row, col)
        self.__tiles = self.__tiles[:p-1] + letter + self.__tiles[p:]

    def get_tiles(self):
        return self.__tiles

    def set_tiles(self, tiles):
        self.__tiles = tiles
        padding = self.__rows * self.__cols - len(tiles)
        self.__tiles = self.__tiles + ("-" * padding) 
        