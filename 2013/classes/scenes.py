"""
/classes/scenes.py
"""
from classes.scene import Scene
from classes.entity import TextEntity


class Scenes(object):
    @staticmethod
    def game_over():
        Scene()
        TextEntity("Game Over")