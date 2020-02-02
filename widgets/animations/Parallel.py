from kivy.animation import Animation as KA
from core.Event import Event

from widgets.animations.Complex import Complex

class Parallel(Complex):
    def __init__(self, **kwargs):
        super(Parallel, self).__init__(**kwargs)

    def do_on_complete(self, *args):
        if self.is_completed():
            self.on_complete(self)

    def is_completed(self):
        return sum([1 for a in self.childs if a.is_completed()]) == len(self.childs)

    def play(self, *args):
        self.__is_completed = False
        for c in self.childs:
            c.play()

    def add_child(self, child):
        super(Parallel, self).add_child(child)
        child.on_complete += self.do_on_complete