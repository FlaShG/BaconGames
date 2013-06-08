import sfml as sf
from classes.entity import Entity

class TileGroup(Entity):

    def __init__(self, width, data, texture):
        self.width = width
        self.data = data
        self.texture = texture
        self.tiles = []
        self.loader()


    def draw(self, window, transform):
        for t in self.tiles:
            window.draw(t, sf.RenderStates(transform=transform.combine(t.transform)))

    def loader(self):
        x = 0
        y = 0

        for d in self.data:
            tile = sf.Sprite(texture)
            tile.texture_rectangle = sf.Rectangle((0, 0), (32, 32))
            tile.position = sf.Vector2(x*32, y*32)
            self.tiles.append() = tile
            if(++x >= self.width):
                x = 0
                ++y



