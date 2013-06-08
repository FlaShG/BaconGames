import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.input import Input
from classes.texturemanager import TextureManager as TM

class TileGroup(Entity):
    def __init__(self, width, data, tilesets, layer):
        super(TileGroup, self).__init__()
        self.width = width
        self.data = data
        self.tilesets = tilesets
        self.tileset = []
        self.loader(layer)


    def loader(self, layer):
        x = 0.0
        y = 0.0

        for d in self.data:
            if(d > 0):
                for t in self.tilesets:
                    if(t['firstgid'] <= d):
                        self.tileset = t
                        break;

                tile = SpriteEntity(texture=TM.get('tiles/' + self.tileset['image']), layer=layer)
                tiles_per_line = self.tileset['imagewidth'] / self.tileset['tilewidth']
                tile_offset = d - self.tileset['firstgid']
                tile.texture_rectangle = sf.Rectangle(
                    (
                        (
                            (tile_offset%tiles_per_line)*32
                        ),
                        (
                            (tile_offset/tiles_per_line)*32
                        )
                    ),
                    (32, 32)
                )

                tile.texture_rectangle
                tile.position = sf.Vector2(x, y)
                self.children.append(tile)

            x += 1.0
            if(x >= self.width):
                x = 0.0
                y += 1.0