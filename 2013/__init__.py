import sfml as sf
from classes.entity import SpriteEntity


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

try:
   # load a sprite to display
   texture = sf.Texture.from_file("rtm.png")
   entity = SpriteEntity(texture=texture)

except IOError: exit(1)

# start the game loop
while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   window.clear() # clear screen
   entity.update(1)
   entity.draw(window)
   window.display() # update the window