from Board import Board

class TerminalBoard(Board):

    def __init__(self, rows, cols):
        super().__init__(rows, cols)

    def draw_tile(self, row, col):
        assert self.inside(row, col)
        letter = self.get_tile(row, col)
        print(letter, end = '') 