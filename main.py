from Game import Game
from TerminalView import TerminalView
import time

if __name__ == "__main__":
    v = TerminalView()
    g = Game(v)
    g.start()
    i = ""
    while i != "x":
        print("touch on? ")
        i = input()
        r, c = [int(n) for n in i.split()]
        g.touch(r, c)
