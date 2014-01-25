"""
Form attributes, ready to tweak.
"""

import resources

def set_form(player, form):
    if form == 'default':
        player.form = form
        player.image = resources.anim_default
        player.jump_speed = 5000
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
    elif form == 'cat':
        player.form = form
        player.image = resources.anim_cat
        player.jump_speed = 5000
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
    elif form == 'elephant':
        player.form = form
        player.image = resources.anim_elephant
        player.jump_speed = 5000
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
    elif form == 'snake':
        player.form = form
        player.image = resources.anim_snake
        player.jump_speed = 5000
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
    elif form == 'bird':
        player.form = form
        player.image = resources.anim_bird
        player.jump_speed = 5000
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
