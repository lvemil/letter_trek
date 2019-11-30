from TerminalBoard import TerminalBoard

if __name__ == "__main__":
    b = TerminalBoard(4,4)
    b.fill_random()
    b.show()
    print()  
    b.set_tile(1,1, 'A')
    b.show()