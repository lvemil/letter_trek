from kivy.animation import Animation as KA

from core.Event import Event

class Animation:
    def __init__(self):
        self.on_complete = Event()

    def play(self):
        pass

    def is_completed(self, *args):
        pass