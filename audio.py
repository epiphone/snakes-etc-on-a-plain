"""
Audio stuff.
"""

import pyglet

fx_bird_death = pyglet.media.load("resources/bird_death.wav", streaming=False)
fx_cat_death = pyglet.media.load("resources/cat_death.wav", streaming=False)
fx_elephant_death = pyglet.media.load("resources/elephant_death.wav", streaming=False)
fx_snake_death = pyglet.media.load("resources/snake_death.wav", streaming=False)
fx_bird_spawn = pyglet.media.load("resources/bird_spawn.wav", streaming=False)
fx_cat_spawn = pyglet.media.load("resources/cat_spawn.wav", streaming=False)
fx_elephant_spawn = pyglet.media.load("resources/elephant_spawn.wav", streaming=False)
fx_snake_spawn = pyglet.media.load("resources/snake_spawn.wav", streaming=False)
elefanttimarssi = pyglet.media.load("resources/elefanttimarssi.wav", streaming=False)
theme = pyglet.media.load("resources/elefanttimarssi.wav", streaming=False)
# fx_snake_death = ...


def death(form):
    """
    Plays the death-sound for given form.
    """
    if form == 'default':
        fx_snake_death.play()
        pass
    elif form == 'bird':
        fx_bird_death.play()
        pass
    elif form == 'elephant':
        fx_elephant_death.play()
        pass
    elif form == 'cat':
        fx_cat_death.play()
        pass

# def joku_toinen_efekti(form):
#  ....
#
def spawn(form):
    """
    Plays the spawn-sound for given form.
    """
    if form == 'default':
        fx_snake_spawn.play()
        pass
    elif form == 'bird':
        fx_bird_spawn.play()

    elif form == 'elephant':
        fx_elephant_spawn.play()
        pass
    elif form == 'cat':
        fx_cat_spawn.play()
        pass

def elefanttimarssi():
    elefanttimarssi.play()

def theme():
    theme.play()