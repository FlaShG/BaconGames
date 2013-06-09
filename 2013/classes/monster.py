"""
/classes/player.py
"""
from classes.entity import Entity, SpriteEntity
from classes.texturemanager import TextureManager as TM
from classes.animation import AnimatorEntity
from classes.collider import Collider
from classes.V2 import V2
import sfml as sf


class Monster(AnimatorEntity):
    def __init__(self):
        pass
        
    def update(self, dt):
        if Player.instance.light_on:
            #Player.instance.position
            pass
            
            