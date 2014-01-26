"""
Thing that flies from a player to another when changing forms.
"""

from physicalobject import PhysicalObject
from utils import distance
import resources

def Swoosh(PhysicalObject):

    def __init__(self, target_player, *args, **kwargs):
        super(Swoosh, self).__init__(
            img=resources.img_swoosh, *args, **kwargs)
        self.target_player = target_player
        self.vel_x, self.vel_y = 0.0, 0.0
        self.reached_target = False

    def update(self, dt):
        dir_x = (self.target_player.x - self.x) / 100.0
        dir_y = (self.target_player.y - self.y) / 100.0

        self.x += dir_x*dt
        self.y += dir_y*dt

        if distance(self.position, self.target_player.position) < 10:
            self.reached_target = True



