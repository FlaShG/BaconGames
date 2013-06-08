from classes.input import Input

class Player(SpriteEntity):
    def __init__(self):
        super(Player, self).__init__(texture=TM.get('player.png'))


    def update(self, dt):
        hor = Input.get_axis('horizontal')
        ver = Input.get_axis('vertical')
        self.move(self, sf.Vector2(hor, ver)*dt)
