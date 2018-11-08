import random
import json
import os

from pico2d import *
import game_framework
import stage4_world
import game_state
name = "Stage_4State"

def enter():
    pass
def exit():
    stage4_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global Start_menu
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                game_framework.pop_state()



def update():
    for game_object in stage4_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in stage4_world.all_objects():
        game_object.draw()
    update_canvas()






