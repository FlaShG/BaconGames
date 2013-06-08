import sfml as sf
import json
from classes.tilegroup import TileGroup
from classes.texturemanager import TextureManager as TM

class TileImporter(object):

    @staticmethod
    def open(filename):
        TileImporter.filename = filename
        TileImporter.file = open(filename)

    @staticmethod
    def parse(file):
        tilegroups = []
        data = json.load(file)

        for l in data['layers']:
            if(l['type'] == 'tilelayer'):
                tilegroups.append(TileGroup(l['width'], l['data'], TM.get(data['tilesets'][0]['image']))