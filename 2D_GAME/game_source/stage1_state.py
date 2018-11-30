import random
import json
import os

from pico2d import *
import game_framework
import stage1_world
import game_state
from stage1 import Back
#from stage1 import Time
from Main_Stage import Time
from stage1 import Shell
name = "Stage_1State"

back =None
time =None
shell =None
on =0
def enter():
    global back,time,shell
    back = Back()
    time = Time()
    shell = Shell()
    stage1_world.add_object(back, 0)
    stage1_world.add_object(time, 0)
    stage1_world.add_object(shell, 1)

def exit():
    stage1_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global shell,on
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT: #R
            on=1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT: #R
            on=4
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT: #B
            on = 2
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT: #B
            on = 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:#G
            on = 3
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:  # G
            on = 6
        else:
            shell.handle_event(event)


def update():
    for game_object in stage1_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in stage1_world.all_objects():
        game_object.draw()
    update_canvas()






