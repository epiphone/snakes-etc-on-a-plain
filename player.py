"""
Player object.
"""

from pyglet.window import key
import resources
from physicalobject import PhysicalObject
from map_objs import Tile, Trap


class Player(PhysicalObject):
    """PhysicalObject with input capabilities."""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.anim_player, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.vel_x, vel_y = 0.0, 0.0
        self.is_falling = False
        self.fall = {
            'speed': 100,
            'multiplier': 1.1
        }
        self.speed = 0
        self.top_speed = 500
        self.speed_multiplier = 1.01
        self.speed_increment = 30
        self.stop_multiplier = 1.05


    def update(self, dt, game_map):

        # Sideways motion:
        if self.key_handler[key.D] or self.key_handler[key.A]:
            if self.key_handler[key.D] and self.key_handler[key.A]:
                self.vel_x = self.vel_x / self.stop_multiplier
            elif self.key_handler[key.D]:
                self.vel_x = min(self.top_speed, self.vel_x + self.speed_increment)


            elif self.key_handler[key.A]:
                self.vel_x = max(-self.top_speed, self.vel_x - self.speed_increment)
        else:
            self.vel_x = self.vel_x / self.stop_multiplier

        if self.key_handler[key.W]:
            pass

        tile_size = game_map.tile_size

        clipped_col_indexes = []
        for col_index, col in enumerate(game_map.get_columns()):
            if col_index * tile_size - game_map.scroll_x > self.x + self.width:
                break
            if col_index * tile_size + tile_size - game_map.scroll_x < self.x:
                continue
            clipped_col_indexes.append(col_index)

        floor_y = None
        for row_index, row in enumerate(game_map.rows):
            row_top_y = (len(game_map.rows) - row_index - 1) * tile_size
            if row_top_y < self.y:
                if any(type(row[col_index]) == Tile for col_index in clipped_col_indexes):
                    floor_y = row_top_y
                    break

        print clipped_col_indexes, floor_y
        if floor_y and self.y + self.vel_y*dt <= floor_y:
            self.vel_y = 0
            self.y = floor_y + 1
        else:
            self.vel_y = -20
            self.y += self.vel_y * dt
        self.x += self.vel_x * dt



        # bottom_obj = None
        # for row_index, row in enumerate(game_map.rows):
        #     if (len(game_map.rows)-row_index)*tile_size + tile_size < self.y:
        #         for col_index in clipped_col_indexes:
        #             if type(row[col_index]) == Tile:
        #                 bottom_obj = row[col_index]
        #                 break

        # if bottom_obj:
        #     if self.y + self.vel_y*dt <= bottom_obj.y + bottom_obj.height:
        #         self.vel_y = 0
        #         self.y = bottom_obj.y + bottom_obj.height + 1
        #     else:
        #         self.vel_y = -50
        # else:
        #     self.y += self.vel_y * dt



        # self.x += self.vel_x * dt

        # clipped_row_indexes = []
        # for row_index in xrange(len(game_map.rows)):
        #     if (len(game_map.rows)-row_index) * tile_size + tile_size < self.y:
        #         break
        #     if (len(game_map.rows)-row_index) * tile_size > self.y + self.height:
        #         continue
        #     clipped_row_indexes.append(row_index)





        # if self.vel_y <= 0:
        #     bounding_border = self.y
        #     bounding_y = None
        #     for row_index, row in enumerate(game_map.rows):
        #         row_top_y = row_index*game_map.tile_size + game_map.tile_size
        #         if row_top_y < bounding_border:
        #             bounding_y = row_top_y
        #         else:
        #             break
        #     a
        #     if bounding_y:
        #         print "bounding_y: ", bounding_y



    def set_falling(self, is_falling):
        if is_falling:
            self.vel_y = -100
        else:
            self.vel_y = 0
        # if self.is_falling:
        #     if is_falling:
        #         self.vel_y *= self.fall['multiplier']
        #     else:
        #         print "stopped falling"
        #         self.vel_y = 0
        # else:
        #     if is_falling:
        #         print "started falling"
        #         self.vel_y = -self.fall['speed']
        #     else:
        #         self.vel_y = 0
        # self.is_falling = is_falling
