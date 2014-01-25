"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet
import maps
from player import Player

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
game_objects = []
scroll_speed = 10
tile_size = 64
game_map = None


def init():
    """
    Initializes the game.
    """
    global game_map
    game_map = maps.Map(maps.map1, main_batch)
    for map_obj in game_map.map_objs:
        if type(map_obj) == Player:
            game_window.push_handlers(map_obj.key_handler)
            game_objects.append(map_obj)



@game_window.event
def on_draw():
    """
    Draws the game world.
    """
    game_window.clear()
    main_batch.draw()


def update(dt):
    """
    Updates the game world by given timestep.
    """
    game_map.scroll_map(dt * scroll_speed)

    player = game_objects[0]  # TODO
    player.update(dt, game_map)
    # collided_x = False
    # collided_y = False
    # is_falling = True



    # for obj in game_map.map_objs:
    #     if type(obj) == Player:
    #         continue
    #     if not collided_y:
    #         if player.bottom_collides(obj):
    #             is_falling = False
    #             collided_y = True
    #             # player.prev_y = obj.y + obj.height + 1
    #             player.y = obj.y + obj.height + 1
    #         elif player.top_collides(obj):
    #             collided_y = True

    #     # if not collided_x:
    #     #     if player.right_collides(obj):
    #     #         collided_x = True
    #     #     elif player.left_collides(obj):
    #     #         collided_x = True

    #     # if collided_y and collided_x:
    #     #     break

    # player.set_falling(is_falling)


def main():
    """
    Initialize and run.
    """
    init()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

