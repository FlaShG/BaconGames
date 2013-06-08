from classes.input import Input
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM
import sfml as sf

class Player(SpriteEntity):
    def __init__(self):
        super(Player, self).__init__(texture=TM.get('player.png'))
        self.speed = 4
        self.light = LightCircle()
        self.light.set_parent(self)


    def update(self, dt):
        hor = Input.get_axis('horizontal')
        ver = Input.get_axis('vertical')
        self.move(sf.Vector2(hor, ver)*dt*self.speed)

class LightCircle(Entity):
    def __init__(self):
        super(LightCircle, self).__init__(layer = 50)
        self.circle = SpriteEntity(texture = TM.get('circle.png'))

    
