"""
Player object.
"""

from pyglet.window import key
import resources
from physicalobject import PhysicalObject
from map_objs import Tile, Trap, Crushable
from form_attrs import set_form
import audio

DEFAULT = 'default'
BIRD = 'bird'
ELEPHANT = 'elephant'
CAT = 'cat'


class Player(PhysicalObject):
    """PhysicalObject with input capabilities."""

    def __init__(self, use_arrow_keys=False, pushes_other_player=False, *args, **kwargs):
        super(Player, self).__init__(img=resources.anim_snake, *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.vel_x, self.vel_y = 0.0, -1.0
        self.form = DEFAULT
        self.is_dead = False
        self.pushes_other_player = pushes_other_player
        self.is_falling = False
        self.is_jumping = False
        self.jump_clicked = False
        self.prev_key = None  # for elephant stomping

        self.set_keys(use_arrow_keys)
        self.set_form(DEFAULT)


    def set_form(self, form=DEFAULT):
        """Toggles between different forms."""
        self.vel_y = -10
        set_form(self, form)


    def set_keys(self, use_arrow_keys):
        if use_arrow_keys:
            self.keys = {
                'up': key.UP,'down': key.DOWN,'left': key.LEFT,'right': key.RIGHT
            }
        else:
            self.keys = {
                'up': key.W, 'down': key.S, 'left': key.A, 'right': key.D
            }

    def get_prioritized_obj(self, objs):
        """
        Returns from a list of objects the object that will be
        handled first. ATM Traps are handled before everything else.
        """
        result = None
        for obj in objs:
            if obj is None or obj.disabled:
                continue
            if type(obj) == Trap:
                return obj
            if type(obj) == Crushable and result is not Crushable:
                result = obj
            elif type(obj) == Tile and result is None:
                result = obj
        return result

    def key(self, key_role):
        return self.key_handler[self.keys[key_role]]

    def stomp(self, new_prev_key=None, increase_speed=False):
        """Helper for elephant stomping."""
        self.prev_key = new_prev_key
        if increase_speed:
            self.vel_x = min(self.top_speed, self.vel_x + self.speed_increment)
        else:
            self.vel_x = self.vel_x / self.stop_multiplier

    def update(self, dt, game_map):
        keys = self.keys

        # Elephant moves by repeating left and right keys:
        if self.form == ELEPHANT and (self.key('left') or self.key('right')):
            if self.key('left') and self.key('right'):
                self.stomp(None, False)
            elif self.prev_key is None:
                self.stomp(self.keys['left'] if self.key('left') else self.keys['right'], True)
            elif self.prev_key == self.keys['left']:
                if self.key('right'):
                    self.stomp(self.keys['right'], True)
                else:
                    self.stomp(self.keys['left'], False)
            elif self.prev_key == self.keys['right']:
                if self.key('left'):
                    self.stomp(self.keys['left'], True)
                else:
                    self.stomp(self.keys['right'], False)
            else:
                self.stomp(None, False)


        else:
            if self.key('left') or self.key('right'):
                if self.key('right') and self.key('left'):
                    self.vel_x = self.vel_x / self.stop_multiplier
                elif self.key('right'):
                    self.vel_x = min(
                        self.top_speed, self.vel_x + self.speed_increment)

                elif self.key('left'):
                    # TODO remove
                    if self.form == ELEPHANT: # elephant can't go left
                        self.vel_x = max(0, self.vel_x-self.speed_increment)
                    else:
                        self.vel_x = max(-self.top_speed, self.vel_x-self.speed_increment)
            else:
                self.vel_x = self.vel_x / self.stop_multiplier

        if self.form == BIRD:
            if self.key('up'):
                self.vel_y = max(100, self.vel_y + 10)
            else:
                self.vel_y = max(-300, self.vel_y - 20)

        else:
            if self.jump_clicked and not self.key_handler[keys['up']]:
                self.jump_clicked = False

            if self.is_jumping:
                self.vel_y -= self.jump_fall_speed*dt
                
                if self.vel_y < 0:
                    self.is_jumping = False
            else:
                if not self.is_falling and not self.jump_clicked and self.key_handler[self.keys['up']]:
                    self.is_jumping = True
                    self.jump_clicked = True
                    self.vel_y = self.jump_speed
                    if self.form == BIRD:
                        if self.image != resources.anim_bird:
                            self.image = resources.anim_bird

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

        if self.vel_y > 0: # Moving up
            top_collider = None
            for row_index, row in enumerate(game_map.rows[::-1]):
                row_bottom_y = row_index * tile_size + 1
                if row_bottom_y >= self.y + self.height:
                    top_colliders = [row[i] for i in clipped_col_indexes]
                    top_collider = self.get_prioritized_obj(top_colliders)
                    if top_collider is not None:
                        break

            if top_collider is None:
                self.y += self.vel_y*dt
            else:
                if self.y + self.height + self.vel_y*dt >= top_collider.y:
                    coll_type = type(top_collider)
                    if self.form == BIRD:
                        self.die()
                    elif coll_type == Tile or (coll_type == Crushable and self.form != ELEPHANT):
                        self.y = top_collider.y - self.height - 1
                    elif coll_type == Crushable:
                        self.crush(top_collider)
                    elif type(top_collider) == Trap:
                        self.die(top_collider)
                else:
                    self.y += self.vel_y*dt

        else: # Moving down
            bottom_collider = None
            for row_index, row in enumerate(game_map.rows):
                row_top_y = (len(game_map.rows) - row_index) * tile_size - 1
                if row_top_y <= self.y:
                    bottom_colliders = [row[i] for i in clipped_col_indexes]
                    bottom_collider = self.get_prioritized_obj(bottom_colliders)
                    if bottom_collider is not None:
                        break

            if bottom_collider is None:
                self.y += self.vel_y*dt
            else:
                if self.y + self.vel_y*dt < bottom_collider.y + tile_size:
                    coll_type = type(bottom_collider)
                    if coll_type==Tile or (coll_type==Crushable and self.form != ELEPHANT):
                        self.y = bottom_collider.y + tile_size
                        self.set_falling(False)
                    elif coll_type == Crushable:
                        self.crush(bottom_collider)
                    elif coll_type == Trap:
                        self.die(bottom_collider)
                else:
                    self.y += self.vel_y * dt
                    self.set_falling(True)
                    #set bird fly anim
                    if self.form == BIRD:
                        if self.image != resources.anim_bird:
                            self.image = resources.anim_bird

        player_real_x_speed = self.vel_x*dt + game_map.scroll_speed*dt
        if player_real_x_speed > 0 and right_coll_col is not None: # Moving right
            right_colliders = [game_map.rows[row_index][right_coll_col]
                               for row_index in clipped_row_indexes]
            right_collider = self.get_prioritized_obj(right_colliders)

            if right_collider is None:
                self.x += self.vel_x*dt
            else:
                future_x = self.x + self.width + self.vel_x*dt
                if future_x >= right_collider.x:
                    coll_type = type(right_collider)
                    if self.form == BIRD:
                        self.die()
                    elif coll_type == Tile or (coll_type == Crushable and self.form != ELEPHANT):
                        self.x = right_collider.x - self.width - 1
                        self.vel_x *= -self.bounce_multiplier
                    elif coll_type == Crushable:
                        self.crush(right_collider)
                    elif coll_type == Trap:
                        self.die(right_collider)
                else:
                    self.x += self.vel_x*dt

        elif player_real_x_speed < 0 and left_coll_col is not None: # Moving left
            left_colliders = [game_map.rows[row_index][left_coll_col]
                              for row_index in clipped_row_indexes]
            left_collider = self.get_prioritized_obj(left_colliders)

            if left_collider is None:
                self.x += self.vel_x*dt
            else:
                future_x = self.x + self.vel_x*dt
                if future_x <= left_collider.x + left_collider.width + 2:
                    coll_type = type(left_collider)
                    if self.form == BIRD:
                        self.die()
                    elif coll_type == Tile or (coll_type==Crushable and self.form != ELEPHANT):
                        self.x = left_collider.x + left_collider.width + 1
                        self.vel_x *= -self.bounce_multiplier
                    elif coll_type == Crushable:
                        self.crush(left_collider)
                    elif coll_type == Trap:
                        self.die(left_collider)
                else:
                    self.x += self.vel_x*dt
        else:
            self.x += self.vel_x*dt


    def on_animation_end(self):
        """Hack to hide self after splatter anim has ended."""
        if self.image == resources.anim_splatter:
            self.position = (-9999, -9999)



    def die(self, collider=None):
        # audio.death(self.form)
        self.is_dead = True
        self.image = resources.anim_splatter


    def crush(self, crushable):
        # audio.crushable(self.form)
        # TODO animation!
        crushable.disabled = True
        crushable.batch = None

    def set_falling(self, is_falling):
        if self.is_falling:
            if is_falling:
                self.vel_y = min(self.fall['multiplier']*self.vel_y,
                                 self.fall['max_speed'])
                # set bird glide anim
                if self.form == BIRD:
                    if self.image != resources.anim_bird_glide:
                        self.image = resources.anim_bird_glide
            else:
                self.vel_y = -self.fall['speed']
        else:
            if is_falling:
                self.vel_y = min(self.fall['multiplier']*self.vel_y,
                                 self.fall['max_speed'])
            else:
                self.vel_y = -self.fall['speed']
        self.is_falling = is_falling
