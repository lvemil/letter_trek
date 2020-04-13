import unittest
from core.Board import Board

class TestBoard(unittest.TestCase):
    def test_IsSolved(self):
        b = Board(4,4)
        b.set_tiles("DIQRGGNAKRYNLB_A")
        assert b.solved("ANGRY")

    def test_Path(self):
        b = Board(3,3)
        b.set_tiles("NLQRERJD_")
        p = b.solved("RED")
        assert len(p) == 3

    def test_FUR(self):
        b = Board(3,3)
        b.fill_random()
        print(b.get_tiles())
        b.set_word("FUR")
        print(b.get_tiles())
        b.mess("FUR")
        print(b.get_tiles())

    def test_NON(self):
        b = Board(3,3)
        b.set_tiles("NXQONRJD_")
        p = b.solved("NON")
        assert len(p) == 3
    def test_Solve(self):
        b = Board(3,3)
        b.set_tiles("WE_MBONRR")
        touches = b.solved("NOW")
        print(touches)

    def test_Solve2(self):
        b = Board(4,4)
        b.set_tiles("EAOAUNMOA_THASMY")
        touches = b.solved("HOMES")
        print(touches)

    def test_solved(self):
        b = Board(3,3)
        b.set_tiles("P_KXFANPR")
        res = b.solved("FAR")
        print(res)