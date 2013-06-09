"""
/classes/soundmanager.py
"""
import sfml as sf

class FontManager():
    fonts = dict()

    @staticmethod
    def get(path):
        try:
            return FontManager.fonts[path]
        except KeyError:
            try:
                font = sf.Font.from_file(path)
                FontManager.fonts[path] = font
                return font
            except IOError:
                print("Could not load font %s!" % path)
                return None
        
