"""
/classes/collider.py
"""

import sfml as sf
from classes.V2 import V2
import math


class Collider(object):
    __all = set()


    def __init__(self, position = sf.Vector2(0,0), size = sf.Vector2(1,1)):
        Collider.__all.add(self)
        self.__position = position
        self.__size = size
        self.recalculate_rect()
        self.peaceful = True
        
       
    @property
    def position(self):
        return self.__position
        
    @position.setter
    def position(self, pos):
        self.__position = pos
        self.recalculate_rect()
        
    @property
    def size(self):
        return self.__size
        
    @size.setter
    def size(self, size):
        self.__size = size
        self.recalculate_rect()
        
    @property
    def radius(self):
        return self.__radius
        
    def recalculate_rect(self):
        self.__rect = sf.Rectangle(self.__position - self.__size/2.0, self.__size)
        self.__radius = max(self.__size.x, self.__size.y) * 2
        
    """
    moves the collider, colliding with others.
    returns the movement delta
    """
    def move_delta(self, dir, recursion_left=3):
        self.peaceful = True
        self.position += dir
    
        if recursion_left > 0:
            for c in Collider.__all:
                dist = c.position - self.position
                if c != self and V2.length(dist) <= self.radius+c.radius:
                    intersection = Collider.intersects(self.__rect, c.__rect)
                    if intersection:
                        #do we have to move into horizontal direction?
                        #horizontal = intersection.width > intersection.height
                        horizontal = math.fabs(dist.x) > math.fabs(dist.y) 
                        #do we have to move into positive direction?
                        positive = (self.position.x > c.position.x) if horizontal else (self.position.y > c.position.y)
                                   
                        sign = 1 if positive else -1
                        
                        dir = sf.Vector2(1,0) if horizontal else sf.Vector2(0,1)
                        dir *= sign
                        
                        return dir + self.move(dir, recursion_left-1)
        else:
            self.peaceful = False

        return dir
        
    """
    moves the collider, colliding with others.
    returns the resulting position
    """
    def move(self, dir, recursion_left=3):
        self.move_delta(dir, recursion_left)
        return self.position
        
        
    def on_collision(self, other):
        pass
        
    def on_trigger(self, other):
        pass
        
        
    @staticmethod
    def intersects(a, b):
        #result = None
        
        #ax2 = a.x + a.width
        #ay2 = a.y + a.height
        #bx2 = b.x + b.width
        #by2 = b.y + b.height
        
        #left = bx2 - a.x
        #right = ax2 - b.x
        #up = by2 - a.y
        #down = ay2 - b.y
        # > 0
        
        #return a.x < bx2 and ax2 > b.x and a.x < by2 and ay2 > b.y
        return a.left < b.right and a.right > b.left and a.top < b.bottom and a.bottom > b.top
        
        
        