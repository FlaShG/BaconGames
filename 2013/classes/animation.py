"""
/classes/animation.py
"""
import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM

class AnimatorEntity(SpriteEntity):

    clips = []
    timer = 0.0
    clip_id = 0
    play_id = 0

    def __init__(self, path, quantity, interval):
        super(AnimatorEntity, self).__init__(texture=TM.get(path + '_0.png'))
        self.gen_clip(path=path, quantity=quantity, interval=interval)


    def play(self, play_id):
        self.play_id = play_id


    def gen_clip(self, path, quantity, interval):
        tmp = []
        for i in range(quantity):
            tmp.append(TM.get(path + '_%d' % i + '.png'))
        self.clips.append(dict(textures=tmp, quantity=quantity, interval=interval))


    def update(self, dt):
        self.timer += dt

        if(self.timer > self.clips[self.play_id]['interval']):
            self.timer = 0.0
            if(self.clip_id == (self.clips[self.play_id]['quantity'] - 1)):
                self.clip_id = 0
            else:
                self.clip_id += 1
            self.sprite.texture = self.clips[self.play_id]['textures'][self.clip_id]