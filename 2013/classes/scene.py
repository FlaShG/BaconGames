import sfml as sf
from classes.entity import Entity

class Scene(object):
    def __init__(self):
        self.entities = []
        self.camera = None
        self.set_camera(Camera())

    def addall(self, entities):
        try:
            for entity in entities:
                self.add(entity)
        except: pass
        
    def add(self, entity):
        if(not entity in self.entities):
            self.entities.append(entity)
        
        
            
    def set_camera(self, camera):
        self.camera = camera
        self.add(camera)


    def process(self, window, dt):
        for e in self.entities:
            e.onupdate(dt)
        for e in self.entities:
            scale = window.height / (20.0 + self.camera.zoom)
            e.ondraw(window, sf.Transform().translate(window.size/2.0 - self.camera.position).scale(sf.Vector2(scale, scale)))

            
class Camera(Entity):
    def __init__(self):
        super(Camera, self).__init__()
        self.zoom = 1