from pico2d import *

import game_framework
import random
import Main_Stage
import stage2_state
import game_state

mario = None
X=[]
Y=[]
count =20
num=0
shape=[0,1,2,1,2,0,1,2,0,2,0,1,2,1,2,0,1,2,0,2]
plus =0

# 시간 설정
# 틀렸을때 -, 깨면 +10
class Back:
    def __init__(self):
        self.image = load_image('game_sprite\\stage2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)


class Hero:
    def __init__(self):
        self.image = load_image('game_sprite\\stage2_item.png')
        self.state =0
        for i in range(0,count):
            Y.append(i*0)
        num=0
        self.hero_sound = load_wav('music\\stage2_hero.wav')
        self.hero_sound.set_volume(32)

    def update(self):
        global X,count,num,shape,plus
        if stage2_state.key ==1:
            self.state = 1#<-
            for i in range(0,num):
               if 1200-X[i] >=10 and 1200-X[i]<=100:
                   if shape[i] ==0:
                        Y[i] =800
                        X[i] =1300
                        self.hero_sound.play()

        elif stage2_state.key ==2:
            self.state = 2#l
            for i in range(0,num):
               if 1200-X[i] >=10 and 1200-X[i]<=100:
                   if shape[i] ==1:
                        Y[i] =800
                        X[i] = 1300
                        self.hero_sound.play()
        elif stage2_state.key ==3:
            self.state = 3#->
            for i in range(0,num):
               if 1200-X[i] >=10 and 1200-X[i]<=100:
                   if shape[i] ==2:
                        Y[i] =800
                        X[i] = 1300
                        self.hero_sound.play()
        elif stage2_state.key ==4 or stage2_state.key ==5  or stage2_state.key ==6:
            self.state = 0
    def draw(self):
        if self.state ==0: #<-
            self.image.clip_draw(80, 250, 90, 130, 1160,1560)
        elif self.state == 1: #l
            self.image.clip_draw(80, 250, 90, 130, 60,560)
        elif self.state == 2: #->
            self.image.clip_draw(80, 250, 90, 130, 60,300)
        elif self.state == 3:
            self.image.clip_draw(80, 250, 90, 130,60,430)


class Bomb:
    def __init__(self):
        global count,num,mario
        self.image = load_image('game_sprite\\stage2_item.png')
        self.bomb_sound = load_wav('music\\stage2_bomb.wav')
        self.bomb_sound.set_volume(32)
        self.error_sound = load_wav('music\\stage2_error.wav')
        self.error_sound.set_volume(32)
        self.clear_sound = load_wav('music\\clear.wav')
        self.clear_sound.set_volume(55)
        for i in range(0,count):
            X.append(i*0)
        self.timer=0
        num=0
    def update(self):
        global X,num,Min_time

        self.timer +=1
        if self.timer %20 ==0:
            self.bomb_sound.play()
            self.timer=0
            num+=1
            if num >20:
               num=20
        for i in range(0, num):
            X[i] += 15
            if X[i] >=1200 and X[i] <1220:
                Main_Stage.min_time += 5
                self.error_sound.play()
            elif X[i] >=1220:
                X[i] =10000
        if X[count-1] >= 10000:
            Main_Stage.plus_time += 10
            self.clear_sound.play()
            game_framework.pop_state()

    def draw(self):
        global X,shape
        for j, i in enumerate(shape):
            if shape[j]==0: #<-
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 560+Y[j])
            elif shape[j] == 1: #l
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 300+Y[j])
            elif shape[j] == 2: #->
                self.image.clip_draw(0, 300, 50, 100, 1200-X[j], 430+Y[j])
