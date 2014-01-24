"""
Loading images and other resources.
"""

import pyglet

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

imgs_player = [pyglet.resource.image('player%d.png' % i) for i in range(2)]
anim_player = pyglet.image.Animation.from_image_sequence(imgs_player, 1.0, True)

img_tile = pyglet.resource.image('tile.png')
