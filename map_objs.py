"""
Tiles, obstacles etc.
"""

from physicalobject import PhysicalObject
import resources

class Tile(PhysicalObject):
    """
    A basic block to run upon. Or crash with.
    """

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.img_tile, *args, **kwargs)

class Trap(PhysicalObject):
    """
    A block that kills player when crashed with.
    """

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(img=resources.trap_tile, *args, **kwargs)


