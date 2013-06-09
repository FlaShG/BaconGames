"""
/classes/player.py
"""
from classes.input import Input
from classes.entity import Entity, SpriteEntity, ScreenSpriteEntity
from classes.texturemanager import TextureManager as TM
from classes.animation import AnimatorEntity
from classes.collider import Collider
from classes.V2 import V2
import sfml as sf


class Player(AnimatorEntity):
    def __init__(self):
        super(Player, self).__init__(path='animations/player/girl_right.png', quantity=2, interval=0.3)
        self.gen_clip(path='animations/player/girl_left.png', quantity=2, interval=0.3)
        self.gen_clip(path='animations/player/girl_top.png', quantity=2, interval=0.3)
        self.gen_clip(path='animations/player/girl_bottom.png', quantity=2, interval=0.3)

        self.speed = 4
        self.light = LightCircle()
        self.light.set_parent(self)

        size = sf.Vector2(1,1)*0.8
        self.collider = Collider(position=self.position, size=size)
        self.scale(size)

    def set_position(self, pos):
        self.position = pos
        self.collider.position = pos

    def update(self, dt):
        super(Player, self).update(dt=dt)
        hor = Input.get_axis('horizontal')
        ver = Input.get_axis('vertical')

        if(hor < 0):
          self.play(1)
        elif(hor > 0):
          self.play(0)
        elif(ver < 0):
          self.play(2)
        elif(ver > 0):
          self.play(3)

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