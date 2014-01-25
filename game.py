"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet
from pyglet.window import key
import maps
import sys

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
game_objects = []
scroll_speed = 10
tile_size = 64
game_map = None


def init(init_map):
    """
    Initializes the game.
    """
    global game_map
    game_map = maps.Map(init_map, main_batch, scroll_speed)
    game_window.push_handlers(game_map.player1.key_handler)
    game_window.push_handlers(game_map.player2.key_handler)


@game_window.event
def on_key_press(symbol, modifiers):
    """
    Handle form changes.
    """
    if symbol == 49:
        game_map.player2.set_form("cat")
    elif symbol == 50:
        game_map.player2.set_form("snake")
    elif symbol == 51:
        game_map.player2.set_form("elephant")
    elif symbol == 52:
        game_map.player2.set_form("bird")
    elif symbol == 109: # M
        game_map.player1.set_form("cat")
    elif symbol == 44:  # ;
        game_map.player1.set_form("snake")
    elif symbol == 46:  # :
        game_map.player1.set_form("elephant")
    elif symbol == 45:  # -
        game_map.player1.set_form("bird")


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
    game_map.scroll_map(dt)

    if not game_map.player1.is_dead:
        game_map.player1.update(dt, game_map)
    if not game_map.player2.is_dead:
        game_map.player2.update(dt, game_map)


def main():
    """
    Initialize and run.
    """
    if len(sys.argv) > 2:
        init(open(sys.argv[-1]).read())
    else:
        init(maps.map1)
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

