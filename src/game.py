"""
Testing out the pyglet library.

Draws heavily from http://steveasleep.com/pyglettutorial.html
"""

import pyglet
from pyglet.window import key
import maps
from utils import distance
import sys
import audio
import resources

game_window = pyglet.window.Window(800, 600)
main_batch = None
game_objects = []
scroll_speed =  130
tile_size = 64
game_map = None
levels = []

displaying_menu = False
menu_batch = None
logo_sprite = None
prompt_sprite = None
prompt_scaler = 1
controls_sprite = None

def init_map(map_to_init=None):
    """
    Initializes the game.
    """
    global game_map, main_batch
    main_batch = pyglet.graphics.Batch()
    map_to_init = map_to_init or levels[0]

    if game_map:
        game_map.delete()  # flushes all sprites

    game_map = maps.Map(map_to_init, main_batch, scroll_speed)
    game_window.remove_handlers()
    game_window.push_handlers(game_map.player1.key_handler)
    game_window.push_handlers(game_map.player2.key_handler)


def init_menu():
    global menu_batch, displaying_menu, logo_sprite, controls_sprite, prompt_sprite
    displaying_menu = True
    menu_batch = pyglet.graphics.Batch()
    logo_sprite = pyglet.sprite.Sprite(resources.img_logo, batch=menu_batch,
        x=game_window.width/2 - resources.img_logo.width/2, y=400)
    controls_sprite = pyglet.sprite.Sprite(resources.img_controls, batch=menu_batch,
        x=game_window.width/2 - resources.img_controls.width/2, y=100)
    prompt_sprite = pyglet.sprite.Sprite(resources.img_prompt, batch=menu_batch,
        x=game_window.width/2 - resources.img_prompt.width/2, y=50)




def load_maps(fname="map%d.txt"):
    global levels
    i = 0
    while True:
        try:
            map_str = open("maps/" + fname % i).read()
            levels.append(map_str)
            i += 1
        except IOError:
            break


@game_window.event
def on_key_press(symbol, modifiers):
    """
    Handle form changes.
    """
    global displaying_menu
    if displaying_menu:  # any key starts game while on menu
        displaying_menu = False
        init_map()

    else:
        if symbol == 49:
            game_map.player2.set_form("default")
        elif symbol == 50:
            game_map.player2.set_form("cat")
        elif symbol == 51:
            game_map.player2.set_form("elephant")
        elif symbol == 52:
            game_map.player2.set_form("bird")
        elif symbol == key.U: # M
            game_map.player1.set_form("default")
        elif symbol == key.I:  # ;
            game_map.player1.set_form("cat")
        elif symbol == key.O:  # :
            game_map.player1.set_form("elephant")
        elif symbol == key.P:  # -
            game_map.player1.set_form("bird")


@game_window.event
def on_draw():
    """
    Draws the game world.
    """
    game_window.clear()
    if displaying_menu:
        menu_batch.draw()
    else:
        main_batch.draw()

can_collide = True


def update(dt):
    """
    Updates the game world by given timestep.
    """
    global can_collide, levels, displaying_menu, prompt_scaler

    if displaying_menu:
        if prompt_sprite.scale > 1.2 or prompt_sprite.scale < 0.8:
            prompt_scaler *= -1
        prompt_sprite.scale += dt*prompt_scaler
        return

    game_map.scroll_map(dt)

    if not game_map.player1.is_dead:
        game_map.player1.update(dt, game_map)
    if not game_map.player2.is_dead:
        game_map.player2.update(dt, game_map)

    if distance(game_map.player1.position, game_map.player2.position) < 50:
        if can_collide:
            audio.bump()
            if abs(game_map.player1.vel_x) > abs(game_map.player2.vel_x):
                game_map.player2.vel_x = game_map.player1.vel_x
                game_map.player1.vel_x *= -1
            else:
                game_map.player1.vel_x = game_map.player2.vel_x
                game_map.player2.vel_x *= -1
            can_collide = False
    else:
        can_collide = True

    for player in [game_map.player1, game_map.player2]:
        if player.x <= -30:
            player.die()

    if game_map.player1.is_dead and game_map.player2.is_dead:
        init_map()

    goal_x = game_map.width - game_map.scroll_x
    if (game_map.player1.x >= goal_x or game_map.player1.is_dead) and (game_map.player2.x >= goal_x or game_map.player2.is_dead):
        if len(levels) == 1:
            print "no more levels"
            sys.exit()
        else:
            levels = levels[1:]
            game_map
            init_map()

    if game_map.player1.form == 'elephant' and game_map.player2.form == 'elephant':
        audio.elefanttimarssi()
    else:
        audio.theme()


def main():
    """
    Initialize and run.
    """
    if len(sys.argv) == 2:
        input_map_str = open(sys.argv[-1]).read()
        init_map(input_map_str)
    else:
        load_maps()
        init_menu()

    pyglet.gl.glClearColor(0.06, 0.51, 0.74, 1)
    audio.theme()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()

