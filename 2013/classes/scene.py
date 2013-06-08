import sfml as sf

class Scene(object):
    def __init__(self):
        self.entities = []

    def add(self, entity):
        try:
            for element in entity:
                self.entities.append(element)
        except:
            self.entities.append(entity)


    def process(self, window, dt):
        for e in self.entities:
            e.onupdate(dt)
        for e in self.entities:
            scale = window.height / 20.0
            e.ondraw(window, sf.Transform().translate(window.size/2.0).scale(sf.Vector2(scale, scale)))
