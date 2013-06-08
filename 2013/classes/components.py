import sfml as sf

class Transform(object):
    def __init__(self):
        self.position = sf.Vector2(0,0)
        self.rotation = 0
        self.scale = sf.Vector2(1,1)
        
    def apply_to(self, thing):
        thing.position = self.position
        thing.rotation = self.rotation
        #thing.scale = self.scale #TODO: Make work with sprites
        
    def __mul__(a,b):
        result = Transform()
        result.position = a.position + b.position #TODO: Make real transform
        result.rotation = a.rotation + b.rotation
        result.scale = a.scale * b.scale
        
        return result