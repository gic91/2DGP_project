import random
import json
import os

from pico2d import *
import game_framework
import stage3_world
import game_state
key =0
#from stage3 import Time
from Main_Stage import Time
from stage3 import Back
from stage3 import Shell
from stage3 import Hero
name = "Stage_3State"
time =None
back =None
shell =None
hero =None
def enter():
    global  time,back,shell,hero
    time = Time()
    back = Back()
    shell = Shell()
    hero  = Hero()
    stage3_world.add_object(back, 0)
    stage3_world.add_object(time, 0)
    stage3_world.add_object(shell, 0)
    stage3_world.add_object(hero, 1)
def exit():
    stage3_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:  # R
            key = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:  # R
            key = 4
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:  # B
            key = 2
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:  # B
            key = 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:  # G
            key = 3
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:  # G
            key = 6



def update():
    for game_object in stage3_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in stage3_world.all_objects():
        game_object.draw()
    update_canvas()






