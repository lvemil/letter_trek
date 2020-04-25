import os

class GamePuzzles:
    def __init__(self):
        self.FILE_NAME = "data/puzzles.txt" 
        self.puzzles = []

    def load(self):
        assert os.path.exists(self.FILE_NAME), "Puzzles file do not exist"
        
        with open(self.FILE_NAME) as file:
            lines = file.readlines()
            data = [tuple(line.strip().split(",")) for line in lines]
            self.puzzles = [(t[0],t[1],int(t[2]),int(t[3]),int(t[4]),int(t[5])) for t in data]

    def get(self, index):
        assert self.puzzles, "puzzles not loaded"
        return self.puzzles[index]