import sfml as sf
from classes.entity import Entity, SpriteEntity

class TileGroup(Entity):
    def __init__(self, width, data, texture):
        super(TileGroup, self).__init__()
        self.width = width
        self.data = data
        self.texture = texture
        self.loader()
        self.scale(sf.Vector2(32,32))


    def loader(self):
        x = 0
        y = 0

        for d in self.data:
            tile = SpriteEntity(texture=self.texture)
            tile.sprite.texture_rectangle = sf.Rectangle((0, 0), (32, 32))
            tile.position = sf.Vector2(x, y)
            self.children.append(tile)
            if(++x >= self.width):
                x = 0
                ++y