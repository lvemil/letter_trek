from core.View import View

class TerminalView(View):
    def draw_tile(self, letter):
        print(letter, end = '')

    def refresh(self):
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                self.draw_tile(self.board.get_tile(r, c))
            print("")
        print(f"Level: {self.level} - Challenge: {self.challenge} - Word: {self.word}")