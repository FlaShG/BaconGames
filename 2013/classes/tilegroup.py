import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.input import Input
from classes.texturemanager import TextureManager as TM

class TileGroup(Entity):
    def __init__(self, width, data, tilesets):
        super(TileGroup, self).__init__()
        self.width = width
        self.data = data
        self.tilesets = tilesets
        self.texture = ''
        self.loader()


    def loader(self):
        x = 0.0
        y = 0.0

        for d in self.data:
            if(d > 0):
                for t in self.tilesets:
                    if(t[0] <= d):
                        self.texture = t[1]
                        break;

                tile = SpriteEntity(texture=TM.get(self.texture))
                tile.texture_rectangle = sf.Rectangle((((d-1)%16)*32, ((d-1)/16)*32), (32, 32))
                tile.texture_rectangle
                tile.position = sf.Vector2(x, y)
                self.children.append(tile)

            x += 1.0
            if(x >= self.width):
                x = 0.0
                y += 1.0