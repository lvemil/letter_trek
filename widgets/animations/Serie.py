from kivy.animation import Animation as KA
from core.Event import Event

from widgets.animations.Complex import Complex

class Serie(Complex):
    def __init__(self, **kwargs):
        super(Serie, self).__init__(**kwargs)
    
    def next(self, *args):
        self.__current += 1
        if self.__current == len(self.childs):
            self.on_complete(self)
        else:
            self.childs[self.__current].play()
        
    def play(self):
        self.__current = -1
        self.next()        

    def add_child(self, child):
        super(Serie, self).add_child(child)
        child.on_complete += self.next