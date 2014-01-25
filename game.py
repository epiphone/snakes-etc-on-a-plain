"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet
import maps

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
game_objects = []
scroll_speed = 200
tile_size = 64
game_map = None


def init():
    """
    Initializes the game.
    """
    global game_map
    game_map = maps.Map(maps.map1, main_batch, scroll_speed)
    game_window.push_handlers(game_map.player1.key_handler)
    game_window.push_handlers(game_map.player2.key_handler)

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
    init()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

