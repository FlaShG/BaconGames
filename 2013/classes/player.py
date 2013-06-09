"""
/classes/player.py
"""
from classes.input import Input
from classes.entity import Entity, SpriteEntity, ScreenSpriteEntity
from classes.texturemanager import TextureManager as TM
from classes.collider import Collider
from classes.V2 import V2
import sfml as sf


class Player(SpriteEntity):
    def __init__(self):
        super(Player, self).__init__(texture=TM.get('player.png'))
        self.speed = 4
        self.light = LightCircle()
        self.light.set_parent(self)
        
        self.collider = Collider(position=self.position)
        

    def set_position(self, pos):
        self.position = pos
        self.collider.position = pos

    def update(self, dt):
        hor = Input.get_axis('horizontal')
        ver = Input.get_axis('vertical')
        input = V2.normalize(sf.Vector2(hor, ver))
        
        self.position = self.collider.move(input * dt * self.speed)
        #self.move(sf.Vector2(hor, ver)*dt*self.speed)
        
        

class LightCircle(Entity):
    def __init__(self):
        super(LightCircle, self).__init__()
        self.circle = ScreenSpriteEntity(texture = TM.get('circle.png'), layer=50, fullscreen=False)
        self.block_left = ScreenSpriteEntity(texture = TM.get('white.png'),
                                             color = sf.Color.BLACK,
                                             layer=50,
                                             fullscreen=False)
        self.block_left.move(sf.Vector2(0.5,0))
        self.block_right = ScreenSpriteEntity(texture = TM.get('white.png'),
                                              color = sf.Color.BLACK,
                                              layer=50,
                                              fullscreen=False)
        self.block_right.move(sf.Vector2(-0.5,0))