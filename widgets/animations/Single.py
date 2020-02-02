from kivy.animation import Animation as KA
from core.Event import Event

from widgets.animations.Animation import Animation

class Single(Animation):
    def __init__(self, kivy_animation, widget, **kwargs):
        super(Single, self).__init__(**kwargs)
        self.__kivy_animation = kivy_animation
        self.__kivy_animation.bind(on_complete = self.do_on_complete)
        self.__widget = widget
    
    def do_on_complete(self, animation, widget):
        self.__is_completed = True
        self.on_complete(self)
        
    def is_completed(self):
        return self.__is_completed

    def play(self):
        self.__is_completed = False
        self.__kivy_animation.start(self.__widget)