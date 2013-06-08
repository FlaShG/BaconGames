import sfml as sf
import json
from classes.tilegroup import TileGroup

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
                tilesets = []
                for t in data['tilesets']:
                    tilesets.append((t['firstgid'], 'tiles/' + t['image']))

                tilesets.sort(key=lambda x: x[0], reverse=True)

                tilegroups.append(TileGroup(l['width'], l['data'], tilesets))

        return tilegroups