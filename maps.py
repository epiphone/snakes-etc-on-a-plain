"""
Everything map-related.
"""

from player import Player
from map_objs import Tile, Trap, Crushable


map1 = """

               v
         xxxxxxx          xxv
x      xx      x      xx
x 1 2                           xxxxxx
xxxxx  h   xx  x   xxx          x
     xxx h xx        x               x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""



class Map(object):
    """A map object with position and drawing."""
    def __init__(self, map_str, batch, scroll_speed=100, tile_size=64):
        self.batch = batch
        self.scroll_speed = scroll_speed
        self.scroll_x = 0
        self.tile_size = tile_size
        self.rows, self.player1, self.player2 = self.parse_map(map_str)
        self.columns = self.get_columns()
        self.height = len(self.rows)*self.tile_size
        self.map_objs = self.get_map_objects()


    def scroll_map(self, dt):
        """
        Updates map objects x coordinate - skips Player objects.
        """
        self.scroll_x += self.scroll_speed * dt
        for row in self.rows:
            for obj in row:
                if obj is not None: #and type(obj) != Player:
                    obj.x -= self.scroll_speed * dt


    def draw(self):
        """
        TODO: skip traversing through null values.
        """
        for row in self.rows:
            for obj in row:
                if obj is not None and type(obj) != Player:
                    obj.draw()


    def parse_map(self, map_str):
        """
        Parses map string into a matrix of map objects.
        """
        map_obj_mapping = {
            '1': Player,
            '2': Player,
            'x': Tile,
            'v': Trap,
            'h': Crushable,
            ' ': None
        }

        player1, player2 = None, None
        lines = [part for part in map_str.split('\n')[1:]]
        lines_len = len(lines)
        max_line_len = len(max(lines, key=len))
        lines = [line + ' '*(max_line_len - len(line)) for line in lines]

        rows = []
        for row_index, line in enumerate(lines):
            row = []
            for col_index, symbol in enumerate(line):
                left_top_x = self.tile_size * col_index
                left_top_y = self.tile_size * (lines_len - row_index)

                obj = map_obj_mapping[symbol]
                if obj is None:
                    row.append(None)
                elif obj == Player:
                    if player1 is None:
                        player1 = Player(x=left_top_x, y=left_top_y -self.tile_size + 1,
                            batch=self.batch)
                        row.append(player1)
                    else:
                        player2 = Player(x=left_top_x, y=left_top_y -self.tile_size + 1,
                            use_arrow_keys=True, batch=self.batch)
                        row.append(player2)
                else:
                    row.append(obj(x=left_top_x, y=left_top_y - self.tile_size + 1,
                        batch=self.batch))
            rows.append(row)

        assert player1 is not None and player2 is not None and type(player1) == Player
        return rows, player1, player2

    def get_columns(self):
        """
        """
        cols = []
        for i in range(len(self.rows[0])):
            col = []
            for row in self.rows:
                col.append(row[i])
            cols.append(col)
        return cols


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
