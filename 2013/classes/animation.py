"""
/classes/animation.py
"""
import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM

class AnimatorEntity(SpriteEntity):

    clip = []
    timer = 0.0
    clip_id = 0

    def __init__(self, path, quantity, interval):
        super(AnimatorEntity, self).__init__(texture=TM.get(path + '_0.png'))
        self.quantity = quantity
        self.path = path
        self.interval = interval
        self.gen_clip()


    def gen_clip(self):
        for i in range(self.quantity):
            self.clip.append(TM.get(self.path + '_%d' % i + '.png'))


    def update(self, dt):
        self.timer += dt

        if(self.timer > self.interval):
            self.timer = 0.0
            if(self.clip_id == (self.quantity - 1)):
                self.clip_id = 0
            else:
                self.clip_id += 1
            self.sprite.texture = self.clip[self.clip_id]