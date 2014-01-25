"""
Audio stuff.
"""

import pyglet

fx_bird_death = pyglet.media.load("resources/audio/old/Birdy death.wav", streaming=False)
fx_cat_death = pyglet.media.load("resources/audio/old/Cat death.wav", streaming=False)
# fx_snake_death = ...


def death(form):
    """
    Plays the death-sound for given form.
    """
    if form == 'default':
        # fx_def_death.play() etc
        pass
    elif form == 'bird':
        fx_bird_death.play()
    elif form == 'snake':
        pass
    elif form == 'elephant':
        pass
    elif form == 'cat':
        pass

# def joku_toinen_efekti(form):
#  ....
#
