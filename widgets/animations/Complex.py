from kivy.animation import Animation as KA
from core.Event import Event

from widgets.animations.Animation import Animation

class Complex(Animation):
    def __init__(self, **kwargs):
        super(Complex, self).__init__(**kwargs)
        self.childs = []
    
    def add_child(self, child):
        self.childs.append(child)