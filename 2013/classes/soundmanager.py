"""
/classes/soundmanager.py
"""
import sfml as sf

class SoundManager():
    sounds = dict()

    @staticmethod
    def get(path):
        try:
            return SoundManager.sounds[path]
        except KeyError:
            try:
                buffer = sf.SoundBuffer.from_file(path)
                sound = sf.Sound(buffer)
                SoundManager.sounds[path] = sound
                return sound
            except IOError:
                print("Could not load sound %s!" % path)
                return None
        
