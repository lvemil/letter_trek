from kivy.core.audio import SoundLoader

class SoundManager:
    def __init__(self):
        pass

    def play(self, name):
        sound = SoundLoader.load(f'assets/{name}.wav')
        if sound:
            sound.volume = 1
            sound.play()