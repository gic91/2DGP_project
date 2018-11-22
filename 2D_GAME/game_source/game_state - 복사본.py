import random
import json
import os

from pico2d import *
import game_framework
import game_world
import stage1_state

from Main_Stage import Stage
from Main_Stage import Item
from Main_Stage import Princess
from Main_Stage import Time
from Main_Stage import Coin
from Mario import Mario

name = "GameState"

Main_Stage=None
item=None
princess =None
main_time=None
mario =None
coin =None
def enter():
    global Main_Stage, item, princess,main_time,mario,coin

    Main_Stage = Stage()
    item = Item()
    princess = Princess()
    main_time = Time()
    mario = Mario()
    coin = Coin()
    game_world.add_object(Main_Stage, 0)
    game_world.add_object(item, 0)
    game_world.add_object(princess, 0)
    game_world.add_object(main_time, 0)
    game_world.add_object(mario, 1)
    game_world.add_object(coin, 0)
def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

        else:
            mario.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






