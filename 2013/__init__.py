"""
/__init__.py
"""
import sfml as sf
from classes.texturemanager import TextureManager as TM
from classes.entity import SpriteEntity
from classes.scene import Scene
from classes.input import Input
from classes.tileimporter import TileImporter
from classes.soundmanager import SoundManager as SM
from classes.player import Player
from classes.collider import Collider
from classes.scenes import Scenes

# create the main window
#window = sf.RenderWindow(sf.VideoMode(640, 480), "Bacon Game")
window = sf.RenderWindow(sf.VideoMode(1024, 768), "Bacon Game")

#scene = Scene()

#TileImporter.open('tiles/tileset.json')
Scenes.game_over()

#Sound-Testing
sound = SM.get('sounds/player_idle_0.ogg')
sound.play()


#SpriteEntity(texture=TM.get('rtm.png')).set_collider(Collider())

#e = SpriteEntity(texture=TM.get('rtm.png'))
#e.set_collider(Collider())
#e.set_position(sf.Vector2(2,-4))
#SpriteEntity(texture=TM.get('rtm.png')).set_parent(e)

#e = ScreenSpriteEntity(texture=TM.get('rtm.png'))
#e.move(sf.Vector2(100,0))

clock = sf.Clock()
Input.define_axis('horizontal', sf.Keyboard.RIGHT, sf.Keyboard.LEFT)
Input.define_axis('vertical', sf.Keyboard.DOWN, sf.Keyboard.UP)

#player = Player()
#scene.camera.set_parent(player)

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
        if type(event) is sf.FocusEvent:
            Input.reset()

    dt = clock.elapsed_time
    clock.restart()

    window.clear() # clear screen
    Scene.current().process(window, dt.seconds)

    window.display() # update the window
