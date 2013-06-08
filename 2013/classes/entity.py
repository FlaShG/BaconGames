import sfml as sf

class Entity(object):
    def __init__(self):
        self.transform = sf.Transform()
        self.enabled = True
        self.children = []

    def onupdate(self, window):
        self.update()
        for c in self.children:
            c.onupdate()
        
    def update(self, dt):
        pass
        
    def ondraw(self, window, transform):
        t = transform * self.transform
        self.draw(window,  t)
        for c in self.children:
            c.ondraw(window, t)
        
    def draw(self, window, transform):
        pass



class VisibleEntity(Entity):
    def __init__(self, color=sf.Color.WHITE):
        super(VisibleEntity, self).__init__()
        
        self.color = color



class SpriteEntity(VisibleEntity):
    def __init__(self, color=sf.Color.WHITE,
                       texture=None,
                       center=sf.Vector2(0.5,0.5)):
        super(SpriteEntity, self).__init__(color)
        
        self.sprite = sf.Sprite(texture)
        self.center = center
        
    def draw(self, window, transform):
        self.sprite.global_bounds = transform.transform_rectangle(sf.Rectangle(sf.Vector2(-0.5,-0.5), sf.Vector2(0.5,0.5))
        #self.sprite.rotation = self.rotation
        
        window.draw(self.sprite)
        
    def update(self, dt):
        self.transform.position.x += dt * 100
        