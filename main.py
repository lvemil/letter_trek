import os
#os.environ['KIVY_AUDIO'] = 'sdl2'

from kivy.config import Config 

import kivy

from LetterTrekApp import LetterTrekApp

if __name__ == "__main__":
    kivy.require('1.11.1')
    app = LetterTrekApp() 
    app.status = "starting"
    app.run()
