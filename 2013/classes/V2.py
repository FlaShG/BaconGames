"""
/classes/V2.py
"""

class V2(object):
    @staticmethod
    def distance(a,b):
        return V2.length(a-b)
        
    @staticmethod
    def length(v):
        return math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2))