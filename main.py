from TerminalBoard import TerminalBoard
import time

if __name__ == "__main__":
    b = TerminalBoard(4,4)
    b.fill_random()
    b.show()
    print()
    start = time.time()
    b.set_word('JULIA')
    print(time.time() - start)
    b.show()
    print()
    start = time.time()
    print(b.solved('JULIA'))
    print(time.time() - start)
    start = time.time()
    b.mess(10)
    print(time.time() - start)
    b.show()
    print()
    print(b.solved('JULIA'))