"""
Form attributes, ready to tweak.
"""

import resources


def set_form(player, form):
    if form == 'default':
        player.image = resources.anim_default
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
        player.image = resources.anim_cat
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
        player.image = resources.anim_elephant
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
        player.image = resources.anim_snake
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
        player.image = resources.anim_bird
        player.top_speed = 500
        player.speed_increment = 30
        player.stop_multiplier = 1.05
        player.bounce_multiplier = 0.3
        player.fall = {
            'speed': 80,
            'multiplier': 1.2,
            'max_speed': 200
        }
