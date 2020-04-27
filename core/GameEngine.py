from core.Board import Board
from core.Event import Event
from core.GameState import GameState
from core.GamePuzzles import GamePuzzles

import pickle
import random

class GameEngine:
    def __init__(self):
        self.LEVEL_COUNT = 20
        self.CHALLENGES_BY_LEVEL = 10
        self.on_board_reset = Event()
        self.on_tile_moved = Event()
        self.on_challenge_completed = Event()
        self.state = GameState()
        self.puzzles = GamePuzzles()
 
    def start(self):
        self.level = 0
        self.next_level()

    def load(self):
        self.state.load()
        self.puzzles.load()
        self.level = self.state.level
        self.challenge = self.state.challenge
        
    def save(self):
        self.state.level = self.level
        self.state.challenge = self.challenge
        self.state.save()

    def get_level_count(self):
        return self.LEVEL_COUNT

    def get_level_progress(self):
        return self.challenge / self.CHALLENGES_BY_LEVEL

    def next_level(self):
        self.level += 1
        self.challenge = 0
        self.next_challenge()

    def set_board(self, puzzle):
        self.board = Board(puzzle[2], puzzle[3])
        self.board.on_tile_moved += self.__on_board_tile_moved
        self.board.set_tiles(puzzle[0])
        
        self.word = puzzle[1] 
        
        # fire on_board_changed event
        self.on_board_reset(self)

    def next_challenge(self):
        # calculate next challenge
        if self.challenge+1 >= self.CHALLENGES_BY_LEVEL:            
            self.level += 1
            self.challenge = -1        
        self.challenge += 1        
        
        # get puzzle
        puzzle_index = (self.level-1) * self.CHALLENGES_BY_LEVEL + self.challenge
        puzzle = self.puzzles.get(puzzle_index)
        
        # set board
        self.set_board(puzzle)

    def check_challenge_completed(self):
        r = self.board.solved(self.word)
        if r == False:
            return False
        else:
            self.solution = r
            return True
        
    def touch(self, row, col):
        return self.board.touch(row, col)

    def __on_board_tile_moved(self, sender, row, col, direction, new_row, new_col):
        self.on_tile_moved(self, row, col, direction, new_row, new_col)