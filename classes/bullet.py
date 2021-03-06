import pyglet
from pyglet.sprite import Sprite
import physicalobject, resources
from config import PLAYER_BULLET_SPEED

class Bullet(physicalobject.PhysicalObject):
    def __init__(self, dy, *args, **kwargs):
        super(Bullet, self).__init__(Sprite(resources.bullet_image, *args, **kwargs))

        #bullets should die after a certain amount of time
        pyglet.clock.schedule_once(self.remove, 1)
        self.velocity_y = dy 

    def clean_up(self):
        self.sprite.delete()
