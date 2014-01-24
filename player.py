"""
Player object.
"""

from pyglet.window import key
import resources
from physicalobject import PhysicalObject


class Player(PhysicalObject):
    """PhysicalObject with input capabilities."""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.anim_player, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.speed = 0
        self.top_speed = 500
        self.speed_multiplier = 1.01
        self.speed_increment = 30
        self.stop_multiplier = 1.05


    def update(self, dt):
        super(Player, self).update(dt)

        # Sideways motion:
        if self.key_handler[key.D] or self.key_handler[key.A]:
            if self.key_handler[key.D] and self.key_handler[key.A]:
                self.vel_x = self.vel_x / self.stop_multiplier
            elif self.key_handler[key.D]:
                # self.vel_x = max(self.vel_x*self.speed_multiplier, self.top_speed)
                self.vel_x = min(self.top_speed, self.vel_x + self.speed_increment)
            elif self.key_handler[key.A]:
                # self.vel_x = min(self.vel_x*self.speed_multiplier, -self.top_speed)
                self.vel_x = max(-self.top_speed, self.vel_x - self.speed_increment)
        else:
            self.vel_x = self.vel_x / self.stop_multiplier

        if self.key_handler[key.W]:
            pass

        #TODO other keys?
