import sfml as sf

class TextureManager():
    textures = dict()

    @staticmethod
    def get(path):
        try:
            return TextureManager.textures[path]
        except KeyError:
            try:
                TextureManager.textures[path] = sf.Texture.from_file(path)
                return TextureManager.textures[path]
            except IOError:
                print("Could not load texture %s!" % path)
                return None
        
