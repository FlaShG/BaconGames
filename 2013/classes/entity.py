import sfml as sf
from classes.input import Input

class Entity(sf.Transformable):
    def __init__(self):
        self.enabled = True
        self.children = []

    def onupdate(self, dt):
        self.update(dt)
        for c in self.children:
            c.onupdate(dt)
            
    def add_child(self, child):
        self.children.append(child)
        
    def update(self, dt):
        pass
        
    def ondraw(self, window, transform):
        #t = transform * self.transform
        t = transform.combine(self.transform)
        self.draw(window,  t)
        for c in self.children:
            c.ondraw(window, t)
        
    def draw(self, window, transform):
        pass



class SpriteEntity(Entity):
    def __init__(self, color=sf.Color.WHITE,
                       texture=None):
        super(SpriteEntity, self).__init__()
        (sf.Sprite, self).__init__(texture=texture)
        
        self.sprite = sf.Sprite(texture)
        ratio = sf.Vector2(1.0 / texture.size.x, 1.0 / texture.size.y)
        self.origin = sf.Vector2(0.5, 0.5)
     
    @property
    def ratio(self):
        return sf.Vector2(self.sprite.ratio.x * self.sprite.texture.size.x,
                          self.sprite.ratio.y * self.sprite.texture.size.y)
    @ratio.setter
    def ratio(self, value):
        self.sprite.ratio = sf.Vector2((value.y*1.0) / self.sprite.texture.size.x,
                                       (value.y*1.0) / self.sprite.texture.size.y)

    @property
    def origin(self):
        return self._origin
    @origin.setter
    def origin(self, value):
        self._origin = value
        self.sprite.origin = sf.Vector2(value.x * self.sprite.texture.size.x,
                                        value.y * self.sprite.texture.size.y)
        
    
    def draw(self, window, transform):
        window.draw(self.sprite, sf.RenderStates(transform=transform))
        