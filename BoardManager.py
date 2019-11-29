class BoardManager:
        def __init__(self, rows = 1, cols = 1):
        self.__rows = rows
        self.__cols = cols
        
    @property
    def rows(self):
        return self.__row
    
    @rows.setter
    def rows(self, rows):
        self.__rows = rows

    @property
    def cols(self):
        return self.__cols
    
    @cols.setter
    def cols(self, cols):
        self.__cols = cols