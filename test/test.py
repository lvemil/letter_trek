import unittest

from core.Board import Board

class TestBoard(unittest.TestCase):
    def test_IsSolved(self):
        b = Board(3,3)
        b.set_tiles("RNZAL_SDW")
        assert b.solved("AS")