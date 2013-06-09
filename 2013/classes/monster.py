"""
/classes/player.py
"""
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM
from classes.animation import AnimatorEntity
from classes.collider import Collider
from classes.V2 import V2
from classes.player import Player
import sfml as sf


class Monster(AnimatorEntity):
    def __init__(self, clip):
        super(Monster, self).__init__(clip)
        
        self.scale
        self.in_light_distance = 6
        self.collider = Collider()
        
         
    def update(self, dt):
        pass
            
    def in_light(self):
        if Player.instance.light_on:
            return V2.distance(Player.instance.position, self.position) <= self.in_light_distance
            
    def direction_to_player(self):
        return Player.instance.position - self.position
        
    def direction_to_player_normalized(self):
        return V2.normalize(self.direction_to_player())
            
class Blob(Monster):
    def __init__(self):
        super(Blob, self).__init__({'path':'animations/player/girl_right.png', 'quantity':2, 'interval':0.2})
        self.speed = 3.5
        self.scale(sf.Vector2(2,2))
        self.collider.size = sf.Vector2(2,2)

    def update(self, dt):
        if self.in_light():
            self.position = self.collider.move(self.direction_to_player_normalized() * self.speed * dt)