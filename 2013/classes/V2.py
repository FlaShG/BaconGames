"""
/classes/V2.py
"""

import math

class V2(object):
    @staticmethod
    def distance(a,b):
        return V2.length(a-b)
        
    @staticmethod
    def length(v):
        return math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2))
        
    @staticmethod
    def normalize(v):
        divisor = V2.length(v)
        return v / divisor if divisor != 0 else v