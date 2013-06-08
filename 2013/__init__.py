import sfml as sf


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")

try:
    # load a sprite to display
    texture = sf.Texture.from_file("rtm.png")
    sprite = sf.Sprite(texture)

    # text
    font = sf.Font.from_file("aller.ttf")
    text = sf.Text("Hello Sascha", font, 50)
    text.position = sf.Vector2(250, 300)


except IOError: exit(1)

# start the game loop
while window.is_open:
    # process events
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()

    window.clear() # clear screen
    window.draw(sprite) # draw the sprite
    window.draw(text)
    window.display() # update the window
