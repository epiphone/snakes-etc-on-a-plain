"""
Contains the PhysicalObject class.
"""

import pyglet
from utils import distance


class PhysicalObject(pyglet.sprite.Sprite):
    """
    A superclass for all physical game objects.
    """
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.event_handlers = []
        self.disabled = False


    def update(self, dt):
        """
        Advances PhysicalObject by given timestep.
        """
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt


    def collides_with(self, other_obj):
        """
        Return True if object collides with another.
        """
        collision_distance = self.width*0.5 + other_obj.width*0.5
        actual_distance = distance(self.position, other_obj.position)

        return actual_distance <= collision_distance

