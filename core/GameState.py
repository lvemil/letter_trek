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
        pass

    def load(self):
        pass