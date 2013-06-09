"""
/classes/collider.py
"""

import sfml as sf
import classes.V2


class Collider(object):
    __all = set()





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
            for c in __all:
                if V2.distance(self.position, c.position) <= self.radius+c.radius:
                    intersection = self.__rect.intersects(c.__rect)
                    if intersection != None:
                        #do we have to move into horizontal direction?
                        horizontal = intersection.width > intersection.height
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
        self.move(dir, recursion_left)
        return self.position


    def on_collision(self, other):
        pass

    def on_trigger(self, other):
        pass
