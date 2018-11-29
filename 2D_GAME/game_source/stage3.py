from pico2d import *

import game_framework
import random
import Main_Stage
import stage3_state
time_time = Main_Stage.time_time


shape = [0,1,2,1,2,0,1,0,2,1,2,0,1,2,1,2,0,1,0,2,1,1,]
count =21
Y = []
for i in range(0, count+1):
    Y.append(i * 150)
class Back:
    def __init__(self):
        self.image = load_image('game_sprite\\stage3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)

class Time:
    def __init__(self):
        self.timer =0
        self.font = load_font('ENCR10B.TTF', 60)
        self.main_time =100
        self.timer2=100
    def update(self):
        global time_time
        self.timer =int(get_time())
        self.main_time = self.timer2 - self.timer
        time_time = self.main_time
        if self.main_time ==0:
            game_framework.quit()
    def draw(self):
        self.font.draw(1060, 670, '%3d' % self.main_time, (255, 0, 0))

class Shell:

    def __init__(self):
        global count
        self.image = load_image('game_sprite\\stage3_item.png')
        self.start=500


    def update(self):
        self.start-=10
        if self.start <=0:
            self.start =0
    def draw(self):
        global shape,Y
        for j, i in enumerate(Y):
            if shape[j] == 0:  # ->
                self.image.clip_draw(212, 255, 60, 200, 790, 200+self.start+Y[j])
            elif shape[j] == 1:  # l
                self.image.clip_draw(108, 255, 60, 200, 610, 200+self.start++Y[j])
            elif shape[j] == 2:  # <-
                self.image.clip_draw(5, 255, 60, 200, 420, 200+self.start+Y[j])
            else:
                self.image.clip_draw(5, 255, 60, 200, 420, 200 + self.start + Y[j])


class Hero:
    def __init__(self):
        self.image = load_image('game_sprite\\stage3_item.png')
        self.state =2
        self.num =1
        self.timer =0
        self.minY=0
        self.HY=[]
        for i in range(0, count+1):
            self.HY.append(i * 0)
        self.hero_sound = load_wav('music\\stage3.wav')
        self.hero_sound.set_volume(32)
        self.error_sound = load_wav('music\\error.wav')
        self.error_sound.set_volume(32)
    def update(self):
        global X,count,num,shape,plus


        if stage3_state.key ==1:
            self.state = 1#<-
            if shape[self.num]==2:
                #if self.timer %40 ==0:
                self.num+=1
                self.hero_sound.play()
                if self.num >= count:
                    game_framework.pop_state()

        elif stage3_state.key ==2:
            self.state = 2#l
            if shape[self.num] == 0:
                #if self.timer % 40 == 0:
                self.num += 1
                self.hero_sound.play()
                if self.num >= count:
                    game_framework.pop_state()

        elif stage3_state.key ==3:
            self.state = 3#->
            if shape[self.num] == 1:
               # if self.timer % 40 == 0:
                self.num += 1
                self.hero_sound.play()
                if self.num >= count:
                    game_framework.pop_state()


        for i in range(0,self.num):
            if self.HY[self.num] >=Y[self.num] :
                for j in range(self.num, count):
                    self.HY[j] = Y[self.num]
            else:
                self.HY[self.num]+=1
                for j in range(0,count):
                    Y[j] = Y[j]- 10




    def draw(self):

        if self.state == 1: #<-
            self.image.clip_draw(6, 150, 40, 75, 420,80+self.HY[self.num]-50)
        elif self.state == 2: #->
            self.image.clip_draw(6, 150, 40, 75, 790,80+self.HY[self.num]-50)
        elif self.state == 3: #l
            self.image.clip_draw(6, 150, 40, 75,610,80+self.HY[self.num]-50)
