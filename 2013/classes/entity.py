import sfml as sf

class Entity(object):
    def __init__(self, position=sf.Vector2(0,0), rotation=0, scale=sf.Vector2(1,1)):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def update(self, dt):
        pass
        
    def draw(self, window):
        pass
        
        
class SpriteEntity(Entity):
    def __init__(self, position=sf.Vector2(0,0), rotation=0, scale=sf.Vector2(1,1), texture=None):
        super(SpriteEntity, self).__init__(position, rotation, scale)
        self.sprite = sf.Sprite(texture)
        
    def draw(self, window):
        self.sprite.position = self.position
        self.sprite.rotation = self.rotation
        window.draw(self.sprite)