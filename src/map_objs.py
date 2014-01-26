"""
Tiles, obstacles etc.
"""

import resources
from physicalobject import PhysicalObject


class Tile(PhysicalObject):
    """
    A basic block to run upon. Or crash with.
    """

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(
            img=resources.img_tile, *args, **kwargs)


class Trap(PhysicalObject):
    """
    A block that kills player when crashed with.
    """

    def __init__(self, *args, **kwargs):
        super(Trap, self).__init__(
            img=resources.anim_spike, *args, **kwargs)


class Crushable(PhysicalObject):
    """
    A block that can be crushed.
    """
    def __init__(self, *args, **kwargs):
        super(Crushable, self).__init__(
            img=resources.img_crushable, *args, **kwargs)

    def destroy(self):
        self.disabled = True
        self.image = resources.anim_crumble

    def on_animation_end(self):
        """Hack to hide self after destroy anim has ended."""
        if self.image == resources.anim_crumble:
            self.batch = None
            self.position = (-9999, -9999)


class Goal(PhysicalObject):
    """
    Goal line indicator.
    """
    def __init__(self, *args, **kwargs):
        super(Goal, self).__init__(
            img=resources.img_goal, *args, **kwargs)
        self.disabled = True




