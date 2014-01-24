"""
Everything map-related.
"""

from physicalobject import PhysicalObject
from player import Player
from map_objs import Tile


map1 = """


p      v
xxxx   xxx
    xxx

"""

class Map(object):
    """A map object with position and drawing."""
    def __init__(self, map_str, batch, tile_size=64):
        self.batch = batch
        self.tile_size = tile_size
        self.rows = self.parse_map(map_str)
        self.map_objs = self.get_map_objects()
        self.scroll_x = 0

    def scroll_map(self, scroll_x):
        """
        Updates map objects x coordinate - skips Player objects.
        """
        self.scroll_x += scroll_x
        for row in self.rows:
            for col_index, obj in enumerate(row):
                if obj is None or type(obj) == Player:
                    continue

                left_top_x = self.tile_size * col_index - self.scroll_x
                obj.x = left_top_x

    def draw(self):
        """
        TODO: skip traversing through null values.
        """
        for obj in self.map_objs:
            obj.draw()


    def parse_map(self, map_str):
        """
        Parses map string into a matrix of map objects.
        """
        map_obj_mapping = {
            'p': Player,
            'x': Tile,
            'v': Trap,
            ' ': None
        }

        lines = [part for part in map_str.split('\n')[1:]]
        lines_len = len(lines)
        max_line_len = len(max(lines, key=len))
        lines = [line + ' '*(max_line_len - len(part)) for line in lines]

        rows = []
        for row_index, line in enumerate(lines):
            row = []
            for col_index, symbol in enumerate(line):
                left_top_x = self.tile_size * col_index
                left_top_y = self.tile_size * (lines_len - row_index)

                obj = map_obj_mapping[symbol]
                if obj is None:
                    row.append(None)
                else:
                    row.append(obj(x=left_top_x, y=left_top_y, batch=self.batch))
            rows.append(row)

        return rows


    def get_map_objects(self):
        """
        Returns a list of all map objects (not Nulls).
        """
        map_objs = []
        for row in self.rows:
            for obj in row:
                if obj is not None:
                    map_objs.append(obj)
        return map_objs







if __name__ == '__main__':
    pass
