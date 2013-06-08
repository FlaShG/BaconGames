import sfml as sf
from classes.entity import Object, Entity

class Scene(Object):
    def __init__(self):
        super(Scene, self).__init__()
        
        Object.root = self
        
        self.entityset = set()
        self.camera = None
        self.set_camera(Camera())

    def add_to_set(self, entity):
        self.entityset.add(entity)

            
    def set_camera(self, camera):
        self.camera = camera
        
    def set_parent(self, parent):
        pass


    def process(self, window, dt):
        for e in self.children:
            e.onupdate(dt)
        for e in self.children:
            scale = window.height / (20.0 + self.camera.zoom)
            e.ondraw(window, sf.Transform().translate(window.size/2.0 - self.camera.position).scale(sf.Vector2(scale, scale)))

            
            
class Camera(Entity):
    def __init__(self):
        super(Camera, self).__init__()
        self.zoom = 1