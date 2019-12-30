class Event():

    def __init__(self):
        self.handlers = []
    
    def add(self, handler):
        self.handlers.append(handler)
        return self
    
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    
    def fire(self, sender, *eargs):
        for handler in self.handlers:
            handler(sender, *eargs)
    
    __iadd__ = add
    __isub__ = remove
    __call__ = fire