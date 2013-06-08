import sfml as sf
from classes.input import Input

class Object(object):
    root = None

    def __init__(self):
        self.children = []
        self.parent = None
        self.set_parent(Object.root)
        
    def set_parent(self, parent):
        if self.parent != None:
            try: self.parent.children.remove(self)
            except: pass
        self.parent = parent
        if self.parent != None:
            parent.children.append(self)
            self.get_root().add_to_set(self)
            
    def get_root(self):
        return self if self.parent == None else self.parent.get_root()
        
    def add_to_set(self):
        pass
            
            

class Entity(Object, sf.Transformable):
    def __init__(self):
        super(Entity, self).__init__()
        self.enabled = True
        self.global_transform = sf.Transform()
        
    def update(self, dt):
        pass
        
    def build_global_transform(self, transform):
        self.global_transform = transform * self.transform
        for c in self.children:
            c.build_global_transform(self.global_transform)
        
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
        window.draw(self.sprite, sf.RenderStates(transform=transform * self.global_transform))
        