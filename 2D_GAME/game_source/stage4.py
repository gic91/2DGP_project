from pico2d import *

import game_framework
import random
import Main_Stage
import stage4_state
COUNT =30

class Back:
    def __init__(self):
        self.image = load_image('game_sprite\\stage4.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)
class Item:
    global COUNT
    def __init__(self):
        self.image = load_image('game_sprite\\stage4_item.png')
        self.left_mush_x=[]
        self.left_mush_y = []
        self.middle_star_x=[]
        self.middle_star_y = []
        self.right_flow_x = []
        self.right_flow_y=[]
        self.left_c=COUNT-1
        self.center_c = COUNT-1
        self.right_c = COUNT-1
        self.mincount=0
        self.switch_1=0
        self.switch_2 = 0
        self.switch_3 = 0
        self.item_sound = load_wav('music\\Balloon.wav')
        self.item_sound.set_volume(50)
        self.clear_sound = load_wav('music\\clear.wav')
        self.clear_sound.set_volume(55)
        for i in range(0, self.left_c):
            self.left_mush_x.append(random.randint(30, 800))
            self.left_mush_y.append(random.randint(30, 750))
        for i in range(0, self.center_c):
            self.middle_star_x.append(random.randint(30, 800))
            self.middle_star_y.append(random.randint(30, 750))
        for i in range(0, self.right_c):
            self.right_flow_x.append(random.randint(30, 800))
            self.right_flow_y.append(random.randint(30, 750))
    def update(self):


        if stage4_state.on == 1:
            self.mincount =1
        elif stage4_state.on == 2:
            self.mincount = 1
        elif stage4_state.on ==3:
            self.mincount = 1
        elif stage4_state.on == 4:
            self.left_c-=self.mincount
            if self.mincount ==1:
                self.item_sound.play()
            self.mincount = 0
            if self.left_c <= 0:
                self.left_c = 0
                self.switch_1 = 1

        elif stage4_state.on == 5:
            self.center_c -= self.mincount
            if self.mincount == 1:
                self.item_sound.play()
            self.mincount = 0

            if self.center_c <= 0:
                self.center_c = 0
                self.switch_2 = 1
        elif stage4_state.on == 6:
            self.right_c -= self.mincount
            if self.mincount == 1:
                self.item_sound.play()
            self.mincount = 0
            if self.right_c <= 0:
                self.right_c = 0
                self.switch_3 = 1
        if self.switch_1==1 and self.switch_2 ==1 and self.switch_3 ==1:
            Main_Stage.plus_time += 10
            self.clear_sound.play()
            game_framework.pop_state()
    def draw(self):
        for i in range(0, self.left_c):
            self.image.clip_draw(0, 300, 70, 100, self.left_mush_x[i], self.left_mush_y[i])
        for i in range(0, self.center_c):
            self.image.clip_draw(80, 300, 70, 100, self.middle_star_x[i], self.middle_star_y[i])
        for i in range(0, self.right_c):
            self.image.clip_draw(160, 300, 70, 100, self.right_flow_x[i], self.right_flow_y[i])
