import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.input import Input
from classes.texturemanager import TextureManager as TM

class TileGroup(Entity):
    def __init__(self, width, data, tilesets, layer):
        super(TileGroup, self).__init__()

        tileset = []
        x = 0.0
        y = 0.0

        for d in data:
            if(d > 0):
                for t in tilesets:
                    if(t['firstgid'] <= d):
                        tileset = t
                        break;

                tile = SpriteEntity(texture=TM.get('tiles/' + tileset['image']), layer=layer)
                tiles_per_line = tileset['imagewidth'] / tileset['tilewidth']
                tile_offset = d - tileset['firstgid']
                tile.texture_rectangle = sf.Rectangle(
                    (
                        (
                            (tile_offset%tiles_per_line)*32 - 0.5
                        ),
                        (
                            (tile_offset/tiles_per_line)*32 - 0.5
                        )
                    ),
                    (31, 31)
                )

                tile.texture_rectangle
                tile.position = sf.Vector2(x, y)
                self.children.append(tile)

            x += 1.0
            if(x >= width):
                x = 0.0
                y += 1.0