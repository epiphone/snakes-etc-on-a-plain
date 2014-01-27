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
music_theme = pyglet.media.load("resources/audio/theme.wav", streaming=False)

music_player = pyglet.media.Player()
music_player.eos_action = pyglet.media.Player.EOS_LOOP
playing_theme = False

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
    # global playing_theme
    # if playing_theme:
    #     music_elefanttimarssi.play()
    global playing_theme
    if playing_theme:
        playing_theme = False
        play_music(music_elefanttimarssi)

def theme():
    global playing_theme
    if not playing_theme:
        playing_theme = True
        play_music(music_theme)
    # if not playing_theme:
    #     playing_theme = True
    #     music_player.queue(music_theme)
    #     music_player.play()

def play_music(source):
    global music_player
    music_player.pause()
    music_player = pyglet.media.Player()
    music_player.eos_action = pyglet.media.Player.EOS_LOOP
    music_player.queue(source)
    music_player.play()
