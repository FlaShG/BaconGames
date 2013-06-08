import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.input import Input

class TileGroup(Entity):
    def __init__(self, width, data, texture):
        super(TileGroup, self).__init__()
        self.width = width
        self.data = data
        self.texture = texture
        self.loader()


    def loader(self):
        x = 0.0
        y = 0.0

        for d in self.data:
            if(d > 0):
                tile = SpriteEntity(texture=self.texture)
                tile.texture_rectangle = sf.Rectangle((((d-1)%16)*32, ((d-1)/16)*32), (32, 32))
                tile.texture_rectangle
                tile.position = sf.Vector2(x, y)
                self.children.append(tile)

            x += 1.0
            if(x >= self.width):
                x = 0.0
                y += 1.0