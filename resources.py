"""
Loading images and other resources.
"""

import pyglet

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

imgs_default = [pyglet.resource.image('player%d.png' % i) for i in range(2)]
anim_default = pyglet.image.Animation.from_image_sequence(imgs_default, 0.05, True)

imgs_cat = [pyglet.resource.image('Cat%d.png' % i) for i in range(2)]
anim_cat = pyglet.image.Animation.from_image_sequence(imgs_cat, 0.05, True)

imgs_elephant = [pyglet.resource.image('Elephant%d.png' % i) for i in range(2)]
anim_elephant = pyglet.image.Animation.from_image_sequence(imgs_elephant, 0.05, True)

imgs_snake = [pyglet.resource.image('Snake%d.png' % i) for i in range(2)]
anim_snake = pyglet.image.Animation.from_image_sequence(imgs_snake, 0.05, True)

imgs_bird = [pyglet.resource.image('Bird%d.png' % i) for i in range(2)]
anim_bird = pyglet.image.Animation.from_image_sequence(imgs_bird, 0.05, True)


img_tile = pyglet.resource.image('tile.png')
img_trap = pyglet.resource.image('trap.png')
img_crushable = pyglet.resource.image('Mud.png')
