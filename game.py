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
game_map = None
tile_size = 64

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
    for obj in game_objects:
        obj.update(dt)
    game_map.scroll_map(dt * scroll_speed)

    # Player falling
    player = game_objects[0]  # TODO
    bottom_y = player.y - tile_size
    left_x, right_x = player.x, player.x + tile_size



def main():
    """
    Initialize and run.
    """
    init()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

