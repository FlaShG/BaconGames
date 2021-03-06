"""
/classes/entity.py
"""
import sfml as sf
from classes.input import Input
from classes.fontmanager import FontManager as FM

class Object(object):
    root = None

    def __init__(self, layer=0):
        self.children = []
        self.__layer = layer
        self.parent = None
        self.set_parent(Object.root)
        
    def set_parent(self, parent):
        if self.parent != None:
            try: self.parent.children.remove(self)
            except: pass
        self.parent = parent
        if self.parent != None:
            parent.children.append(self)
            self.get_root().add_to_set(self, self.layer)
            
    def set_layer(self, layer):
        self.get_root().add_to_set(self, layer)
        self.__layer = layer
        
    @property
    def layer(self):
        return self.__layer
            
    def get_root(self):
        return self if self.parent == None else self.parent.get_root()
        
    def add_to_set(self, entity, layer):
        pass
            
            

class Entity(Object, sf.Transformable):
    def __init__(self, layer=0):
        super(Entity, self).__init__(layer)
        self.enabled = True
        self.global_transform = sf.Transform()
        self.collider = None
        
    def update(self, dt):
        pass
        
    def build_global_transform(self, transform):
        self.global_transform = transform * self.transform
        for c in self.children:
            c.build_global_transform(self.global_transform)

    def ondraw(self, window, transform):
        if self.enabled:
            self.draw(window, transform)
  
    def draw(self, window, transform):
        pass
        
    def set_position(self, position):
        self.position = position
        if self.collider != None:
            self.collider.position = position
            
    def set_collider(self, collider):
        self.collider = collider
        if collider != None:
            collider.position = self.position


class SpriteEntity(Entity):
    def __init__(self, layer=0,
                       color=sf.Color.WHITE,
                       texture=None):
        super(SpriteEntity, self).__init__(layer)
        (sf.Sprite, self).__init__(texture=texture)
        
        self.sprite = sf.Sprite(texture)
        self.sprite.color = color
        self.ratio = sf.Vector2(1.0, 1.0)
        self.origin = sf.Vector2(0.5, 0.5)
        self.__renderstate = sf.RenderStates()
     
    @property
    def ratio(self):
        return self._ratio
        
    @ratio.setter
    def ratio(self, value):
        self._ratio = value
        if self.texture_rectangle.width == 0 or self.texture_rectangle.height == 0:
            self.sprite.ratio = sf.Vector2(1,1)
        else:
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
        self.__renderstate.transform = transform * self.global_transform
        window.draw(self.sprite, self.__renderstate)
        
        
class ScreenSpriteEntity(SpriteEntity):
    def __init__(self, layer=0,
                       color=sf.Color.WHITE,
                       texture=None,
                       fullscreen=True):
        super(ScreenSpriteEntity, self).__init__(layer, color, texture)
        self.fullscreen = fullscreen
        
        self.__renderstate = sf.RenderStates()
        
        
    def draw(self, window, transform):
        position = self.position
        fullscreen_offset = ((window.height*2.0) - 1)
        self.global_transform.translate(sf.Vector2(position.x * fullscreen_offset, position.y * fullscreen_offset))
        
        self.sprite.ratio = self.windowed_ratio(window)
        t = sf.Transform().translate(window.size / 2.0)
        
        self.__renderstate.transform = transform = t * self.global_transform
        
        window.draw(self.sprite, self.__renderstate)
        
        self.position = position

        
    def windowed_ratio(self, window):
        return sf.Vector2((self._ratio.x*1.0) / self.texture_rectangle.width * (window.width if self.fullscreen else window.height),
                                              (self._ratio.y*1.0) / self.texture_rectangle.height * window.height)
                                              

class TextEntity(Entity):
    def __init__(self, text):
        super(TextEntity, self).__init__()
        self.text = sf.Text(text)
        
        self.text.font = FM.get("fonts/toscuchet.otf")
        self.text.color = sf.Color.WHITE
        self.text.character_size = 72
        
        self.__renderstate = sf.RenderStates()
        
        
    def draw(self, window, transform):
        scale = sf.Vector2(window.width / 768.0, window.height / 768.0)
        t = sf.Transform().scale(sf.Vector2(1,1) * scale.y)
        scaled_bounds = sf.Vector2(self.text.local_bounds.size.x * scale.y, self.text.local_bounds.size.y * scale.y)
        t.translate((window.size - scaled_bounds) / 2.0)
    
        self.__renderstate.transform = t * self.global_transform
        window.draw(self.text, self.__renderstate)
        
        