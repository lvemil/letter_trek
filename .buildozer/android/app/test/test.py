import unittest

from core.Board import Board

class TestBoard(unittest.TestCase):
    def test_IsSolved(self):
        b = Board(4,4)
        b.set_tiles("DIQRGGNAKRYNLB_A")
        assert b.solved("ANGRY")

    def test_FUR(self):
        b = Board(3,3)
        b.fill_random()
        print(b.get_tiles())
        b.set_word("FUR")
        print(b.get_tiles())
        b.mess("FUR")
        print(b.get_tiles())
