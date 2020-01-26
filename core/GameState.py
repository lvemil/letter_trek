import pickle
import os

class GameState:
    
    def __init__(self):
        self.level = 0
        self.challenge = 0 

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def challenge(self):
        return self.__challenge

    @challenge.setter
    def challenge(self, challenge):
        self.__challenge = challenge

    def save(self):
        data = {
            "challenge":self.challenge, 
            "level": self.level
        }
        with open('data/state.pkl','wb',) as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        fn = 'data/state.pkl'
        
        if os.path.exists(fn) == False:
            self.level = 0
            self.challenge = 0
            self.save()
        else:
            with open('data/state.pkl','rb') as f:
                data = pickle.load(f)
                self.level = data["level"]
                self.challenge = data["challenge"]