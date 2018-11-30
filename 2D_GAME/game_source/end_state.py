import random
import json
import os

from pico2d import *
import game_framework
import game_state
import menu_state
name = "End_State"

def enter():
    global image_1,image_2,image_3,image_4,end_sound,Time_count,Menu
    image_1 = load_image('game_sprite\\time_over_1.png')
    image_2 = load_image('game_sprite\\time_over_2.png')
    end_sound= load_music('music\\Game over.wav')
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
       if Menu==1:
            if event.type == SDL_QUIT:
                game_framework.quit()



def update():
   global Time_count,Menu
   Time_count += 0.1
   if Time_count >= 40:
       end_sound.stop()
       game_framework.quit()


def draw():
    global image_1, image_2, image_3, image_4,Time_count,on
    clear_canvas()
    if Menu==0:
        if int(Time_count) %10>5:
            image_2.draw(600, 400)
        else:
            image_1.draw(600, 400)

    update_canvas()


