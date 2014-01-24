"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
game_objects = []

score_label = pyglet.text.Label(
    text='Score: 0', x=10, y=575, batch=main_batch)


def init():
    """
    Initializes the game.
    """
    game_objects.append()

@game_window.event
def on_draw():
    """
    Draws the game world.
    """
    game_window.clear()
    score_label.draw()


def update(dt):
    """
    Updates the game world by given timestep.
    """
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
