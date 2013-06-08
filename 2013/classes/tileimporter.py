import sfml as sf
import json
from classes.tilegroup import TileGroup
from classes.texturemanager import TextureManager as TM

class TileImporter():
    @staticmethod
    def open(filename):
        return TileImporter.parse(open(filename))

    @staticmethod
    def parse(file):
        tilegroups = []
        data = json.load(file)

        for l in data['layers']:
            if(l['type'] == 'tilelayer'):
                tilegroups.append(TileGroup(l['width'], l['data'], TM.get(data['tilesets'][0]['image'])))

        return tilegroups