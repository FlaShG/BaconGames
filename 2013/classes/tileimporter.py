"""
/classes/tileimporter.py
"""
import sfml as sf
import json
from classes.tilegroup import TileGroup
from classes.entity import Entity
from classes.collider import Collider

class TileImporter():
    @staticmethod
    def open(filename):
        return TileImporter.parse(open(filename))

    @staticmethod
    def parse(file):
        tilegroups = []
        data = json.load(file)

        layer = -100

        tilesets = []
        for t in data['tilesets']:
            tilesets.append(t)

        tilesets.sort(key=lambda x: x['firstgid'], reverse=True)
        
        for l in data['layers']:
            if(l['type'] == 'tilelayer'):
                if(l['name'] == 'gamelogic'):
                    layer = 1
                    TileImporter.gamelogic(l, tilesets)
                else:
                    tilegroups.append(TileGroup(l['width'], l['data'], tilesets, layer))
                    layer += 1

    @staticmethod
    def gamelogic(layer, tilesets):
        x = 0
        y = 0
    
        for data in layer['data']:
            if data > 0:
                for t in tilesets:
                    if(t['firstgid'] <= data):
                        tileset = t
                        break;
                        
                id = data - t['firstgid'] +1
                
                if id==1:
                    c = Entity()
                    c.set_collider(Collider())
                    c.set_position(sf.Vector2(x,y))
                
            x += 1
            if(x >= layer['width']):
                x = 0
                y += 1
