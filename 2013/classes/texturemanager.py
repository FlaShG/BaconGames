import sfml as sf

class TextureManager():
    textures = dict()

    @staticmethod
    def get(path):
        try:
            return TextureManager.textures[path]
        except KeyError:
            TextureManager.textures[path] = sf.Texture.from_file(path)
            return TextureManager.textures[path]
        
