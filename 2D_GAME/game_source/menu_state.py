import random
import json
import os

from pico2d import *
import game_framework
import game_world
import menu_world
import game_state


from Start_menu import Menu

name = "MenuState"

boy = None
Start_menu = None
menu_time =None
def enter():
    global Start_menu
    Start_menu = Menu()
    menu_world.add_object(Start_menu, 0)

def exit():
    menu_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global Start_menu,menu_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif Start_menu.start ==1:
                menu_time =get_time()
                game_framework.change_state(game_state)

                #game_framework.quit()
        else:
            Start_menu.handle_event(event)


def update():
    for game_object in menu_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in menu_world.all_objects():
        game_object.draw()
    update_canvas()






