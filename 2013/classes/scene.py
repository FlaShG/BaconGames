import sfml as sf
from components import Transform

class Scene(object):
    def __init__(self):
        self.entities = []
        
    def add(self, entity):
        self.entities.append(entity)
    
    def process(self, window, dt):
        for e in self.entities:
            e.onupdate(dt)
        for e in self.entities:
            e.ondraw(window, Transform())
