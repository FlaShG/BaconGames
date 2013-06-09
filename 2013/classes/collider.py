"""
/classes/collider.py
"""

import sfml as sf

class Collider(object):
    __all = set()


    def __init__(self, position = sf.Vector2(0,0),
                       size = sf.Vector2(1,1))
        __all.add(self)
        self.__position = position
        self.__rect = sf.Rectangle(-size/2.0, size/2.0)
        
       
    @property
    def position(self):
        return self.__position
        
    @position.setter
    def position(self, pos):
        self.__position = pos
        self.recalculate_rect()
        
    def recalculate_rect(self):
        self.__rect = sf.Rectangle(self.__position - self.__size/2.0, self.__size)
        self.__radius = self.__size * 2
        
    
    def move(self, dir):
        
        
    def on_collision(self, other):
        pass
        
    def on_trigger(self, other):
        pass
        