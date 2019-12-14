from TerminalBoard import TerminalBoard
from Game import Game
from View import View
import time

if __name__ == "__main__":
    v = View()
    g = Game(v)
    g.start()
    i = ""
    while i != "x":
        print("touch on? ")
        i = input()
        r, c = [int(n) for n in i.split()]
        g.touch(r, c)
