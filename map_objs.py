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
            img=resources.img_trap, *args, **kwargs)


class Crushable(PhysicalObject):
    """
    A block that can be crushed.
    """
    def __init__(self, *args, **kwargs):
        super(Crushable, self).__init__(
            img=resources.img_crushable, *args, **kwargs)


