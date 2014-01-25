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
        self.vel_x, self.vel_y = 0.0, -1.0
        self.is_falling = False
        self.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
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
                self.vel_x = min(
                    self.top_speed, self.vel_x + self.speed_increment)

            elif self.key_handler[key.A]:
                self.vel_x = max(
                    -self.top_speed, self.vel_x - self.speed_increment)
        else:
            self.vel_x = self.vel_x / self.stop_multiplier

        if self.key_handler[key.W]:
            pass

        tile_size = game_map.tile_size
        right_coll_col, left_coll_col = None, None

        clipped_col_indexes = []
        for col_index, col in enumerate(game_map.get_columns()):
            if col_index * tile_size - game_map.scroll_x > self.x + self.width:
                right_coll_col = col_index
                break

            if col_index * tile_size + tile_size - game_map.scroll_x < self.x:
                left_coll_col = col_index
                continue
            clipped_col_indexes.append(col_index)

        bottom_collides_with = None
        floor_y = None
        for row_index, row in enumerate(game_map.rows):
            row_top_y = (len(game_map.rows) - row_index) * tile_size
            if row_top_y < self.y:
                bottom_colliders = [row[col_index] for col_index in clipped_col_indexes]
                for obj in bottom_colliders:
                    if type(obj) == Tile and bottom_collides_with is None:
                        bottom_collides_with = obj
                    elif type(obj) == Trap:
                        bottom_collides_with = obj
                if bottom_collides_with is not None:
                    break

                # if any(type(obj) == Trap for obj in bottom_colliders):
                #     bottom_collides_with = obj
                # elif any(type(obj) == Tile for obj in bottom_colliders):
                #     floor_y = row_top_y
                #     bottom_collides_with = obj
                # if bottom_collides_with:
                #     break
        if bottom_collides_with is None:
            self.x += self.vel_x * dt
            self.y += self.vel_y * dt

        elif type(bottom_collides_with) == Trap:
            print "hit a trap!"
        else:
            if self.y + self.vel_y*dt <= bottom_collides_with.y + tile_size:
                self.y = bottom_collides_with.y + tile_size + 1
                self.set_falling(False)
            else:
                self.y += self.vel_y * dt
                self.set_falling(True)
            self.x += self.vel_x * dt


    def set_falling(self, is_falling):
        if self.is_falling:
            if is_falling:
                self.vel_y = min(self.fall['multiplier']*self.vel_y, self.fall['max_speed'])
            else:
                print "stopped falling"
                self.vel_y = -self.fall['speed']
        else:
            if is_falling:
                print "started falling"
                self.vel_y = min(self.fall['multiplier']*self.vel_y, self.fall['max_speed'])
            else:
                self.vel_y = -self.fall['speed']
        self.is_falling = is_falling
