from View import View

class TerminalView(View):
    def draw_tile(self, letter):
        print(letter, end = '')

    def refresh(self):
        for r in range(self.__board.rows):
            for c in range(self.__board.cols):
                self.draw_tile(self.__board.get_tile(r, c))
            print("")
        print(f"Word: {self.__word}")