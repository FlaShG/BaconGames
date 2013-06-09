"""
/classes/animation.py
"""
import sfml as sf
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM

class AnimatorEntity(SpriteEntity):

    def __init__(self, clip):
        super(AnimatorEntity, self).__init__(texture=TM.get(clip['path']))
        self.clips = []
        self.clip_id = 0
        self.play_id = 0
        self.gen_clip(clip=clip)
        self.timer = 100


    def play(self, play_id):
        if(play_id != self.play_id):
            self.play_id = play_id
            self.timer = 100


    def gen_clip(self, clip):
        path = clip['path']
        quantity = clip['quantity']
        interval = clip['interval']
        self.clips.append(dict(texture=TM.get(path), quantity=quantity, interval=interval))


    def update(self, dt):
        self.timer += dt

        if(self.timer > self.clips[self.play_id]['interval']):
            self.timer = 0.0
            self.sprite.texture = self.clips[self.play_id]['texture']
            self.texture_rectangle = sf.Rectangle((self.clip_id * 32, 0), (32, 32))

            if(self.clip_id == (self.clips[self.play_id]['quantity'] - 1)):
                self.clip_id = 0
            else:
                self.clip_id += 1
