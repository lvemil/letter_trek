from functools import partial

from kivy.animation import Animation as KA
from kivy.clock import Clock

class Sequence:
    def __init__(self, clock: Clock):
        self.__animations = []
        self.__clock = clock

    def add_animation(self, animation: KA, widget, start):
        self.__animations.append((animation, widget, start))

    def clock_callback(self, a, w, *largs):
        a.start(w)

    def play(self):
        for a, w, s in self.__animations:
            self.__clock.schedule_once(partial(self.clock_callback, a, w), s)

    def duration(self):
        return sum([s for _, _, s in self.__animations])