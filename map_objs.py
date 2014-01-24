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
        super(Tile, self, *args, **kwargs)
        self.img = resources.img_tile

