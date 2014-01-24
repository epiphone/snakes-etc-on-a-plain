"""
Contains the PhysicalObject class.
"""

import pyglet


class PhysicalObject(pyglet.sprite.Sprite):
    """
    A superclass for all physical game objects.
    """
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.event_handlers = []


    def update(self, dt):
        """
        Advances PhysicalObject by given timestep.
        """
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
