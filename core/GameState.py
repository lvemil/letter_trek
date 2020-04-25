import pickle
import os

class GameState:
    
    def __init__(self):
        self.level = 0
        self.challenge = 0 
        #self.tiles = ""
        #self.rows = 0
        #self.cols = 0

    def save(self):
        data = {
            "challenge":self.challenge, 
            "level": self.level,
            #"tiles": self.tiles,
            #"rows": self.rows,
            #"cols": self.cols 
        }
        with open('data/state.pkl','wb',) as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        fn = 'data/state.pkl'
        
        if os.path.exists(fn) == False:
            self.level = 1
            self.challenge = -1
            """ self.rows = 0
            self.cols = 0
            self.tiles = "" """
            self.save()
        else:
            with open('data/state.pkl','rb') as f:
                data = pickle.load(f)
                self.level = data["level"]
                self.challenge = data["challenge"]
                """ self.rows = data["rows"]
                self.cols = data["cols"]
                self.tiles = data["tiles"] """