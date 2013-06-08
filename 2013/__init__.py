import sfml as sf
from classes.texturemanager import TextureManager as TM
from classes.entity import SpriteEntity
from classes.scene import Scene
from classes.input import Input
from classes.tileimporter import TileImporter
from classes.player import Player

# create the main window
#window = sf.RenderWindow(sf.VideoMode(640, 480), "Bacon Game")
window = sf.RenderWindow(sf.VideoMode(1024, 768), "Bacon Game")

scene = Scene()

tiles = TileImporter.open('tiles/tileset.json')
scene.addall(tiles)

clock = sf.Clock()
Input.define_axis('horizontal', sf.Keyboard.RIGHT, sf.Keyboard.LEFT)
Input.define_axis('vertical', sf.Keyboard.UP, sf.Keyboard.DOWN)

scene.add(Player())

# start the game loop
while window.is_open:
    Input.update()
   # process events
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            Input.process_event(event)

    dt = clock.elapsed_time
    clock.restart()

    window.clear() # clear screen
    scene.process(window, dt.seconds)

    window.display() # update the window
