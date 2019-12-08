from TerminalBoard import TerminalBoard
from Game import Game
import time

if __name__ == "__main__":
    g = Game()
    g.start()
    i = ""
    while i != "x":
        print("touch on? ")
        i = input()
        r, c = [int(n) for n in i.split()]
        g.touch(r, c)
