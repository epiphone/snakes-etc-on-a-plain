"""
Audio stuff.
"""

import pyglet

fx_bird_death = pyglet.media.load("resources/audio/bird_death.wav", streaming=False)
fx_cat_death = pyglet.media.load("resources/audio/cat_death.wav", streaming=False)
fx_elephant_death = pyglet.media.load("resources/audio/elephant_death.wav", streaming=False)
fx_snake_death = pyglet.media.load("resources/audio/snake_death.wav", streaming=False)
fx_bird_spawn = pyglet.media.load("resources/audio/bird_spawn.wav", streaming=False)
fx_cat_spawn = pyglet.media.load("resources/audio/cat_spawn.wav", streaming=False)
fx_elephant_spawn = pyglet.media.load("resources/audio/elephant_spawn.wav", streaming=False)
fx_snake_spawn = pyglet.media.load("resources/audio/snake_spawn.wav", streaming=False)

fx_crushable = pyglet.media.load("resources/audio/death.wav", streaming=False)
fx_bump = pyglet.media.load("resources/audio/hit.wav", streaming=False)

music_elefanttimarssi = pyglet.media.load("resources/audio/elefanttimarssi.wav", streaming=False)
music_theme = pyglet.media.load("resources/audio/theme.mp3", streaming=False)

music_player = pyglet.media.Player()
music_player.eos_action = pyglet.media.Player.EOS_LOOP

def bump():
    """
    Players collide with each other.
    """
    fx_bump.play()


def crushable():
    """
    Elephant crushes a tile.
    """
    fx_crushable.play()


def death(form):
    """
    Plays the death-sound for given form.
    """
    if form == 'default':
        fx_snake_death.play()
    elif form == 'bird':
        fx_bird_death.play()
    elif form == 'elephant':
        fx_elephant_death.play()
    elif form == 'cat':
        fx_cat_death.play()

def spawn(form):
    """
    Plays the spawn-sound for given form.
    """
    if form == 'default':
        fx_snake_spawn.play()
    elif form == 'bird':
        fx_bird_spawn.play()
    elif form == 'elephant':
        fx_elephant_spawn.play()
    elif form == 'cat':
        fx_cat_spawn.play()

def elefanttimarssi():
    music_elefanttimarssi.play()

def theme():
    music_player.queue(music_theme)
    music_player.play()
