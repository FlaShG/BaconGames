import sfml as sf

class Scene(object):
    def __init__(self):
        self.entities = []
        
    def add(self, entity):
        self.entities.append(entity)
    
    def process(self, window, dt):
        for e in self.entities:
            e.update(dt)
        for e in self.entities:
            e.draw(window)
