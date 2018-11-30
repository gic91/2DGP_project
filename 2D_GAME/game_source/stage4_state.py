import random
import json
import os

from pico2d import *
import game_framework
import stage4_world
import game_state
from stage4 import Back
from stage4 import Item
from Main_Stage import Time
name = "Stage_4State"

back =None
item = None
time =None
on =0
def enter():
    global back,item,time
    back = Back()
    item = Item()
    time = Time()
    stage4_world.add_object(back, 0)
    stage4_world.add_object(time, 0)
    stage4_world.add_object(item, 1)
def exit():
    stage4_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global Start_menu,on
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:  # R
            on = 1

        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:  # R
            on = 4
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:  # B
            on = 2
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:  # B
            on = 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:  # G
            on = 3
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:  # G
            on = 6



def update():
    for game_object in stage4_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in stage4_world.all_objects():
        game_object.draw()
    update_canvas()


