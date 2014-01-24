"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()
score_label = pyglet.text.Label(
    text="Score: 0", x=10, y=575, batch=main_batch)


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
    pass

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()