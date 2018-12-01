import random
import json
import os

from pico2d import *
import game_framework
import game_state
import menu_state
name = "clear_State"
import Main_Stage



def enter():
    global image_1,end_sound,Time_count,Menu,font,font2
    image_1 = load_image('game_sprite\\game clear.png')
    end_sound= load_music('music\\ending_clear.mp3')
    font = load_font('ENCR10B.TTF', 200)
    font2 = load_font('ENCR10B.TTF', 100)
    end_sound.set_volume(64)
    end_sound.repeat_play()
    Time_count = 0
    Menu=0

def exit():
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global Menu
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.quit()


def update():
    pass

def draw():
    global image_1,font,font2
    clear_canvas()
    image_1.draw(600, 400)
    font2.draw(770, 570, ' GAME ', (0, 0, 150))
    font2.draw(730, 470, ' CLEAR!', (0, 0, 150))
    font.draw(730, 270, '%3d' %  Main_Stage.end_time, (0, 0, 150))
    update_canvas()


