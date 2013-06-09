"""
/classes/collider.py
"""

import sfml as sf
from classes.V2 import V2
import math


class Collider(object):
    __all = set()

    def __init__(self, position = sf.Vector2(0,0), size = sf.Vector2(1,1), offset = sf.Vector2(0,0)):
        Collider.__all.add(self)
        self.__offset = offset
        self.__size = size
        self.position = position #must use setter!
        #self.recalculate_rect()
        self.peaceful = True
        
        self.event_handler = None

    @property
    def position(self):
        return self.__position - self.offset

    @position.setter
    def position(self, pos):
        self.__position = pos + self.offset
        self.recalculate_rect()
        
    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset
        self.__position = pos + self.offset
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
        self.__rect = sf.Rectangle(self.__position - self.size/2.0, self.size)
        self.__radius = max(self.size.x, self.size.y) * 2

    """
    moves the collider, colliding with others.
    returns the movement delta
    """
    def move_delta(self, direction, recursion_left=3):
        self.peaceful = True
        self.position += direction

        if recursion_left > 0:
            for c in Collider.__all:
                dist = c.position - self.position
                if c != self and V2.length(dist) <= self.radius+c.radius:
                    r1 = self.__rect
                    r2 = c.__rect
                    intersects, dir = Collider.intersects(r1, r2)
                    if intersects:
                        self.on_collision(c)
                        c.on_collision(self)
                        """
                        #do we have to move into horizontal direction?
                        #horizontal = intersection.width > intersection.height
                        horizontal = math.fabs(dist.x) / ((r1.width+r2.width)/2.0) > math.fabs(dist.y) / ((r1.height+r2.height)/2.0) 
                        #do we have to move into positive direction?
                        positive = (self.position.x > c.position.x) if horizontal else (self.position.y > c.position.y)

                        sign = 1 if positive else -1

                        dir = sf.Vector2(1,0) if horizontal else sf.Vector2(0,1)
                        dir *= sign
                        """
                        
                        if dir.x == 1:
                            dir.x = r2.right - r1.left
                        elif dir.x == -1:
                            dir.x = r2.left - r1.right
                        elif dir.y == 1:
                            dir.y = r2.bottom - r1.top
                        elif dir.y == -1:
                            dir.y = r2.top - r1.bottom
                            
                            
                        return direction + self.move(dir, recursion_left-1)
        else:
            self.peaceful = False

        return direction

    """
    moves the collider, colliding with others.
    returns the resulting position
    """
    def move(self, dir, recursion_left=3):
        self.move_delta(dir, recursion_left)
        return self.position


    def on_collision(self, other):
        if self.event_handler != None:
            self.event_handler.on_collision(other)

    def on_trigger(self, other):
        pass

        
    @staticmethod
    def intersects(a, b):
        #return a.x < bx2 and ax2 > b.x and a.x < by2 and ay2 > b.y
        #return a.left < b.right and a.right > b.left and a.top < b.bottom and a.bottom > b.top
        
        if a.left < b.right and a.right > b.left and a.top < b.bottom and a.bottom > b.top:
        
            v = sf.Vector2(a.right - b.right + a.left - b.left, a.top - b.top + a.bottom - b.bottom)
            
            if math.fabs(v.x) > math.fabs(v.y):
                v.x = 1 if v.x > 0 else -1
                v.y = 0
            else:
                v.x = 0
                v.y = 1 if v.y > 0 else -1
            
            return True, v
                
        else:
            return False, sf.Vector2(0,0)


        
        