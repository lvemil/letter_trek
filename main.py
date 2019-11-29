from BoardManager import BoardManager

if __name__ == "__main__":
    mb = BoardManager(4,4)
    mb.set_tiles("12345678")
    print(mb.get_tiles())
    mb.set_tile(1,1, 'A')
    print(mb.get_tiles())