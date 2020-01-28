from kivy.animation import Animation as KA
from core.Event import Event

class Animation:
    def __init__(self):
        self.on_complete = Event()

    def play(self):
        pass

    def is_completed(self, *args):
        pass

class Single(Animation):
    def __init__(self, kivy_animation, widget, **kwargs):
        super(Single, self).__init__(**kwargs)
        self.__kivy_animation = kivy_animation
        self.__kivy_animation.bind(on_complete = self.__on_complete)
        self.__widget = widget
    
    def __on_complete(self):
        self.__is_completed = True
        self.on_complete()
        
    def is_completed(self):
        return self.__is_completed

    def play(self):
        self.__is_completed = False
        self.__kivy_animation.start(self.__widget)

class Complex(Animation):
    def __init__(self, **kwargs):
        super(Complex, self).__init__(**kwargs)
        self.childs = []
    
    def add_child(self, child):
        self.childs.append(child)

class Parallel(Complex):
    def __init__(self, **kwargs):
        super(Parallel, self).__init__(**kwargs)

    def __on_complete(self):
        if self.is_completed():
            self.on_complete()

    def is_completed(self):
        return sum([1 for a in self.childs if a.is_completed]) == len(self.childs)

    def play(self, *args):
        self.__is_completed = False
        for c in self.childs:
            c.play()

    def add_child(self, child):
        super(Parallel, self).add_child(child)
        child.on_complete += self.__on_complete

class Serie(Complex):
    def __init__(self, **kwargs):
        super(Serie, self).__init__(**kwargs)
    
    def next(self):
        self.__current += 1
        if self.__current == len(self.childs)-1:
            self.on_complete()
        else:
            self.childs[self.__current].play()
        
    def play(self):
        self.__current = -1
        self.next()        

    def add_child(self, child):
        super(Serie, self).add_child(child)
        child.on_complete += self.next