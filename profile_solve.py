from core.BoardSolver import BoardSolver
from core.Board import Board

def main():
    b = Board(4,4)
    b.set_tiles("LYCHFJCMEMVVOTG_")
    bs = BoardSolver()
    touches = bs.psolve2(b, "HEFTY")
    print(touches)

def main3():
    b = Board(4,4)
    b.set_tiles("EAOAUNMOA_THASMY")
    bs = BoardSolver()
    touches = bs.solve2(b, "HOMES")
    print(touches)

def main2():
    b = Board(3,3)
    b.set_tiles("WE_MBONRR")
    bs = BoardSolver()
    touches = bs.solve2(b, "NOW")
    print(touches)

if __name__ == '__main__':
    main()