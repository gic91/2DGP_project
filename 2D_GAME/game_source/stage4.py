from pico2d import *

import game_framework
import random
import Main_Stage
import stage4_state
import Mario
time_time = Main_Stage.time_time
Min_time= Main_Stage.min_time

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
        self.left_c=COUNT
        self.center_c = COUNT
        self.right_c = COUNT
        self.switch_1=0
        self.switch_2 = 0
        self.switch_3 = 0
    def update(self):
        for i in range(0, self.left_c):
            self.left_mush_x.append(random.randint(30, 800))
            self.left_mush_y.append(random.randint(30, 750))
        for i in range(0, self.center_c):
            self.middle_star_x.append(random.randint(30, 800))
            self.middle_star_y.append(random.randint(30, 750))
        for i in range(0, self.right_c):
            self.right_flow_x.append(random.randint(30, 800))
            self.right_flow_y.append(random.randint(30, 750))

        if stage4_state.on == 1:
            self.left_c -= 1
            if self.left_c <=0:
                self.left_c =0
                self.switch_1=1
        elif stage4_state.on == 2:
            self.center_c -= 1
            if self.center_c <=0:
                self.center_c =0
                self.switch_2 = 1
        elif stage4_state.on ==3:
            self.right_c -= 1
            if self.right_c <=0:
                self.right_c =0
                self.switch_3 = 1
        elif stage4_state.on == 4:
            pass
        elif stage4_state.on == 5:
            pass
        elif stage4_state.on == 6:
           pass
        if self.switch_1==1 and self.switch_2 ==1 and self.switch_3 ==1:
            Mario.dir=1
            game_framework.pop_state()
    def draw(self):
        for i in range(0, self.left_c):
            self.image.clip_draw(0, 300, 70, 100, self.left_mush_x[i], self.left_mush_y[i])
        for i in range(0, self.center_c):
            self.image.clip_draw(80, 300, 70, 100, self.middle_star_x[i], self.middle_star_y[i])
        for i in range(0, self.right_c):
            self.image.clip_draw(160, 300, 70, 100, self.right_flow_x[i], self.right_flow_y[i])
class Time:
    def __init__(self):
        self.timer =0
        self.font = load_font('ENCR10B.TTF', 60)
        self.main_time =100
        self.timer2=100
        self.min_time=0
    def update(self):
        global time_time,Min_time
        self.timer =int(get_time())
        self.main_time = self.timer2 - self.timer -Min_time
        Main_Stage.min_time =Min_time
        time_time = self.main_time
        if self.main_time ==0:
            game_framework.quit()
    def draw(self):
        self.font.draw(1060, 670, '%3d' % self.main_time, (255, 0, 0))


