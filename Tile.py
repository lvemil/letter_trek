class Tile:
    def __init__(self, color = "", row = 1, col = 1):
        self.__letter = color
        self.__row = row
        self.__col = col
        
    @property
    def row(self):
        return self.__row
    
    @row.setter
    def row(self, row):
        self.__row = row

    @property
    def col(self):
        return self.__col
    
    @col.setter
    def col(self, col):
        self.__col = col    
    
    @property
    def letter(self):
        return self.__letter
    
    @letter.setter
    def letter(self, letter):
        self.__letter = letter 