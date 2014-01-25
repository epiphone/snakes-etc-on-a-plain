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

    def bottom_collides(self, other):
        """
        Returns True if object's bottom collides with another object.
        """
        if self.x > other.x + other.width or self.x + self.width < other.x:
            return False
        # return abs(self.y - (other.y + other.height)) <= threshold
        return self.y <= (other.y + other.height) < self.prev_y

    def top_collides(self, other):
        threshold = abs(self.vel_y)
        if self.x > other.x + other.width or self.x + self.width < other.x:
            return False
        return abs(other.y - (self.y + self.height)) <= threshold

    def left_collides(self, other):
        threshold = abs(self.vel_x)
        if self.y > other.y + other.height or self.y + self.height < other.y:
            return False
        return abs(self.x - (other.x + other.width)) <= threshold

    def right_collides(self, other):
        threshold = abs(self.vel_x)
        if self.y > other.y + other.height or self.y + self.height < other.y:
            return False
        return abs(other.x - (self.x + self.width)) <= threshold



    def is_touchable_by(self, other):
        """
        Returns a list with 4 boolean values:
        [top, right, bottom, left]
        """
        threshold_y = self.vel_y + 4
        threshold_x = self.vel_x + 4

        if self.x > other.x + other.width + threshold_x or self.x + self.width + threshold_x < other.x:
            return None
        if self.y > other.y + other.height + threshold_y or self.y + self.height + threshold_y < other.y:
            return None

        return True
