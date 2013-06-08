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
        #self.scale(sf.Vector2(3,3))
        
        #self.scale(sf.Vector2(0.1,0.1))


    def loader(self):
        x = 0.0
        y = 0.0

        for d in self.data:
            tile = SpriteEntity(texture=self.texture)
            tile.texture_rectangle = sf.Rectangle((0, 0), (32,32))
            tile.position = sf.Vector2(x, y)
            print(x,y)
            self.children.append(tile)
            x += 1.0
            if(x >= self.width):
                x = 0.0
                y += 1.0