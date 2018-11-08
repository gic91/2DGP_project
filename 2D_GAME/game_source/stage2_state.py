import random
import json
import os

from pico2d import *
import game_framework
import stage2_world
import game_state
from stage2 import Back
from stage2 import Time
from stage2 import Hero
from stage2 import Bomb
name = "Stage_2State"
key =0
back =None
time =None
hero = None
bomb =None
def enter():
    global back,time,bomb
    back = Back()
    time = Time()
    hero = Hero()
    bomb = Bomb()
    stage2_world.add_object(back, 0)
    stage2_world.add_object(time, 0)
    stage2_world.add_object(hero, 1)
    stage2_world.add_object(bomb, 1)
def exit():
    stage2_world.clear()

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
    for game_object in stage2_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in stage2_world.all_objects():
        game_object.draw()
    update_canvas()






