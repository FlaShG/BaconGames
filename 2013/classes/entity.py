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
        t = transform * self.transform
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
        self.ratio = sf.Vector2(1.0, 1.0)
        self.origin = sf.Vector2(0.5, 0.5)
     
    @property
    def ratio(self):
        return self._ratio
        
    @ratio.setter
    def ratio(self, value):
        self._ratio = value
        #self.sprite.ratio = sf.Vector2((value.x*1.0) / (self.sprite.texture.width / self.texture_rectangle.width),
        #                               (value.y*1.0) / (self.sprite.texture.height / self.texture_rectangle.height))
        #self.sprite.ratio = sf.Vector2((value.x*1.0) / self.sprite.texture.width,
        #                               (value.y*1.0) / self.sprite.texture.height)
        self.sprite.ratio = sf.Vector2((value.x*1.0) / self.texture_rectangle.width,
                                       (value.y*1.0) / self.texture_rectangle.height)                             
                                       
    @property
    def texture_rectangle(self):
        return self.sprite.texture_rectangle
    @texture_rectangle.setter
    def texture_rectangle(self, value):
        ratio = self.ratio
        self.sprite.texture_rectangle = value
        self.ratio = ratio
        self.origin = self._origin
                           
    @property
    def origin(self):
        return self._origin
    @origin.setter
    def origin(self, value):
        self._origin = value
        self.sprite.origin = sf.Vector2(value.x * self.texture_rectangle.size.x,
                                        value.y * self.texture_rectangle.size.y)
        
    
    def draw(self, window, transform):
        window.draw(self.sprite, sf.RenderStates(transform=transform))
        