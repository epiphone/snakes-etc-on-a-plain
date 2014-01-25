"""
Player object.
"""

from pyglet.window import key
import resources
from physicalobject import PhysicalObject
from map_objs import Tile, Trap
# import utils

class Player(PhysicalObject):
    """PhysicalObject with input capabilities."""

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.anim_player, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.vel_x, self.vel_y = 0.0, -1.0

        self.is_falling = False
        self.is_jumping = False
        self.jump_clicked = False

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
        self.bounce_multiplier = 0.3


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


        if self.jump_clicked and not self.key_handler[key.W]:
            self.jump_clicked = False

        if self.is_jumping:
            self.vel_y -= 5000*dt
            if self.vel_y < 0:
                self.is_jumping = False
        else:
            if not self.is_falling and not self.jump_clicked and self.key_handler[key.W]:
                self.is_jumping = True
                self.jump_clicked = True
                self.vel_y = 1200


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

        clipped_row_indexes = []
        for row_index, row in enumerate(game_map.rows):
            row_bottom_y = (len(game_map.rows) - row_index - 1) * tile_size
            if row_bottom_y > self.y + self.height - 2: # adjust 2?
                continue # row bottom is higher than player top
            if row_bottom_y + tile_size < self.y:
                break # row top is lower than player bottom
            clipped_row_indexes.append(row_index)

        if self.vel_y > 0:
            self.y += self.vel_y*dt
        else:
            bottom_collides_with = None
            for row_index, row in enumerate(game_map.rows):
                row_top_y = (len(game_map.rows) - row_index) * tile_size
                if row_top_y < self.y:
                    bottom_colliders = [row[i] for i in clipped_col_indexes]
                    for obj in bottom_colliders:
                        if type(obj) == Tile and bottom_collides_with is None:
                            bottom_collides_with = obj
                        elif type(obj) == Trap:
                            bottom_collides_with = obj
                    if bottom_collides_with is not None:
                        break

            if bottom_collides_with is None:
                self.y += self.vel_y * dt
            else:
                if self.y + self.vel_y*dt <= bottom_collides_with.y + tile_size:
                    if type(bottom_collides_with) == Tile:
                        self.y = bottom_collides_with.y + tile_size
                        self.set_falling(False)
                    elif type(bottom_collides_with) == Trap:
                        print "hit a trap!"
                else:
                    self.y += self.vel_y * dt
                    self.set_falling(True)

        player_real_x_speed = self.vel_x*dt + game_map.scroll_speed*dt

        if player_real_x_speed > 0 and right_coll_col is not None: # Moving right
            right_collider = None
            right_colliders = [game_map.rows[row_index][right_coll_col]
                               for row_index in clipped_row_indexes]
            for obj in right_colliders:
                if type(obj) == Trap:
                    right_collider = obj
                    break
                if type(obj) == Tile and right_collider is None:
                    right_collider = obj

            if right_collider is None:
                self.x += self.vel_x*dt
            else:
                future_x = self.x + self.width + self.vel_x*dt # - game_map.scroll_speed*dt
                if future_x >= right_collider.x - game_map.scroll_speed*dt:
                    if type(right_collider) == Tile:
                        self.x = right_collider.x - self.width - game_map.scroll_speed*dt-1
                        self.vel_x *= -self.bounce_multiplier
                    elif type(right_collider) == Trap:
                        print "right hit a trap!"
                else:
                    self.x += self.vel_x*dt

        elif player_real_x_speed < 0 and left_coll_col is not None: # Moving left
            left_colliders = [game_map.rows[row_index][left_coll_col]
                              for row_index in clipped_row_indexes]
            left_collider = None
            for obj in left_colliders:
                if type(obj) == Tile and left_collider is None:
                    left_collider = obj
                elif type(obj) == Trap:
                    left_collider = obj
                    break

            if left_collider is None:
                self.x += self.vel_x*dt
            else:
                future_x = self.x + self.vel_x*dt + game_map.scroll_speed*dt
                if future_x <= left_collider.x + left_collider.width:
                    if type(left_collider) == Tile:
                        self.x = left_collider.x + left_collider.width + game_map.scroll_speed*dt + 1
                        self.vel_x *= -self.bounce_multiplier
                    elif type(left_collider) == Trap:
                        print "left hit a trap!"
                else:
                    self.x += self.vel_x*dt
        else:
            self.x += self.vel_x*dt



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
