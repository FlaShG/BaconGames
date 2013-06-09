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
    instance = None

    def __init__(self):
        super(Player, self).__init__({'path':'animations/player/girl_right.png', 'quantity':2, 'interval':0.2})

        self.light_circle = LightCircle()
        
        self.no_light_circle = ScreenSpriteEntity(texture=TM.get('white.png'),
                                                  color=sf.Color.BLACK,
                                                  fullscreen=True,
                                                  layer=51)
        self.no_light_circle.enabled = False
        self.light_on = True

        Player.instance = self
        
        self.speed = 2.5
        
        self.gen_clip({'path':'animations/player/girl_left.png', 'quantity':2, 'interval':0.2})
        self.gen_clip({'path':'animations/player/girl_top.png', 'quantity':2, 'interval':0.2})
        self.gen_clip({'path':'animations/player/girl_bottom.png', 'quantity':2, 'interval':0.2})
        
        collider_height = 0.3
        self.collider = Collider(position=self.position,
                                 size=sf.Vector2(0.2,collider_height),
                                 offset=sf.Vector3(0,(1-collider_height)/2.0))
        self.scale(sf.Vector2(1,1)*0.8)

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


        if Input.get_key_down(sf.Keyboard.SPACE):
            self.light_on = not self.light_on
            self.no_light_circle.enabled = not self.light_on
            Player.instance.set_layer(80 if not self.light_on else 0)
            self.sprite.color = sf.Color.WHITE if self.light_on else sf.Color(128,128,128)
        

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

