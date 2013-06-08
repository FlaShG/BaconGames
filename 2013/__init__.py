import sfml as sf
from classes.entity import SpriteEntity
from classes.scene import Scene


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

scene = Scene()


try:
    # load a sprite to display
    texture = sf.Texture.from_file("rtm.png")
    entity = SpriteEntity(position=sf.Vector2(200,200), texture=texture)
    scene.add(entity)

except IOError: exit(1)

clock = sf.Clock()

# start the game loop
while window.is_open:
   # process events
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()

    dt = clock.elapsed_time
    clock.restart()
    
    window.clear() # clear screen
    scene.process(window, dt.seconds)

    window.display() # update the window
