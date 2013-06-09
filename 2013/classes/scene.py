"""
/classes/scene.py
"""
import sfml as sf
from classes.entity import Object, Entity
from collections import OrderedDict

class Scene(Object):
    def __init__(self):
        super(Scene, self).__init__()
        
        Object.root = self
        
        self.entityset = OrderedDict()
        self.layer_change_list = dict()
        
        self.camera = None
        self.set_camera(Camera())

        

    def add_to_set(self, entity, layer = 0):
        #print("Adding to Layer %i" % layer)
        self.layer_change_list[entity] = (entity.layer, layer)


            
    def set_camera(self, camera):
        self.camera = camera
        
    def set_parent(self, parent):
        pass


    def process(self, window, dt):
        for layer in self.entityset:
            for e in self.entityset[layer]:
                e.update(dt)
                
        for entity in self.layer_change_list:
            change = self.layer_change_list[entity]
            from_layer = change[0]
            to_layer = change[1]
            try:
                self.entityset[from_layer].remove(entity)
            except: pass
            
            if not to_layer in self.entityset:
                self.entityset[to_layer] = set()
                self.entityset = OrderedDict(sorted(self.entityset.items(), key=lambda t: t[0]))
                
            self.entityset[to_layer].add(entity)
            
        self.layer_change_list = dict()

            
        for e in self.children:
            e.build_global_transform(sf.Transform())
                
        scale = window.height / (16.0 + self.camera.zoom)
        transform = sf.Transform().translate(window.size/2.0)
        transform = transform.scale(sf.Vector2(scale, scale)) * self.camera.global_transform.inverse
            
        for layer in self.entityset:
            for e in self.entityset[layer]:
                e.ondraw(window, transform)
                
    @staticmethod
    def current():
        return Object.root
            
            
class Camera(Entity):
    def __init__(self):
        super(Camera, self).__init__()
        self.zoom = 1
