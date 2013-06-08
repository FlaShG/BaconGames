import sfml as sf
from classes.entity import SpriteEntity
from classes.scene import Scene


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

scene = Scene()


try:
    # load a sprite to display
    texture = sf.Texture.from_file("rtm.png")
    entity = SpriteEntity(texture=texture)
    entity.position = sf.Vector2(10,10)
    entity.ratio = sf.Vector2(50,50)
    scene.add(entity)
    
    entity2 = SpriteEntity(texture=texture)
    entity2.position = sf.Vector2(10,400)
    entity2.rotation = 180
    entity2.ratio = sf.Vector2(60,60)
    entity.add_child(entity2)

    
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
