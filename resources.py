"""
Loading images and other resources.
"""

import pyglet

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

imgs_cat = [pyglet.resource.image('Cat%d.png' % i) for i in range(2)]
anim_cat = pyglet.image.Animation.from_image_sequence(imgs_cat, 0.05, True)

imgs_elephant = [pyglet.resource.image('Elephant%d.png' % i) for i in range(2)]
anim_elephant = pyglet.image.Animation.from_image_sequence(imgs_elephant, 0.05, True)

imgs_snake = [pyglet.resource.image('Snake%d.png' % i) for i in range(2)]
subimgs_snake = [img.get_region(0, 0, 64, 35) for img in imgs_snake]
anim_snake = pyglet.image.Animation.from_image_sequence(subimgs_snake, 0.05, True)

imgs_bird = [pyglet.resource.image('Bird%d.png' % i) for i in range(2)]
anim_bird = pyglet.image.Animation.from_image_sequence(imgs_bird, 0.05, True)

imgs_splatter = [pyglet.resource.image('BloodExplosion%d.png' % i) for i in range(2)]
anim_splatter = pyglet.image.Animation.from_image_sequence(imgs_splatter, 0.175, True)

img_swoosh = pyglet.resource.image('MudTop.png')
img_tile = pyglet.resource.image('tile.png')
img_trap = pyglet.resource.image('trap.png')
img_crushable = pyglet.resource.image('Mud.png')
