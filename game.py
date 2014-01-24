"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet
import resources
from player import Player

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
game_objects = []

def init():
    """
    Initializes the game.
    """
    player = Player(img=resources.anim_player, batch=main_batch, x=100, y=100)
    game_window.push_handlers(player.key_handler)
    game_objects.append(player)

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


def main():
    """
    Initialize and run.
    """
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

