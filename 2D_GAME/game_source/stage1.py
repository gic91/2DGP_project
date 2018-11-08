from pico2d import *

import game_framework
import random
import Main_Stage
import stage1_state

time_time = Main_Stage.time_time

Min_time= Main_Stage.min_time

class Back:
    def __init__(self):
        self.image = load_image('game_sprite\\stage1.png')

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
        self.min_time=0
    def update(self):
        global time_time,Min_time
        self.timer =int(get_time())
        self.main_time = self.timer2 - self.timer -Main_Stage.min_time
        time_time = self.main_time
        if self.main_time ==0:
            game_framework.quit()
    def draw(self):
        self.font.draw(1060, 670, '%3d' % self.main_time, (255, 0, 0))


class Shell:

    def __init__(self):
        self.image = load_image('game_sprite\\shell.png')
        self.Count =10
        self.out_on=[False]
        self.Y=[]
        self.X=[]
        self.color=[1,0,1,2,0,1,2,0,1,2]
        for i in range(0,self.Count):
            #self.color.append(random.randint(0,2))
            self.Y.append(i*200)
            self.X.append(i*0)
        self.start=500
        self.num=0
        self.min_time=0
        self.min_counter=False
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        global Min_time
        self.start-=10
        if self.start <=0:
            self.start =0
        if stage1_state.on == 1:
            if self.color[self.num]==0 :
                self.num += 1
                if self.num >= self.Count:
                    self.num += 0
                    game_framework.pop_state()
            else:
                self.min_counter =True

        elif stage1_state.on == 2:
            if self.color[self.num] == 1:
                self.num += 1
                if self.num >= self.Count:
                    self.num += 0
                    game_framework.pop_state()
            else:
                self.min_counter = True
        elif stage1_state.on == 3:
            if self.color[self.num] == 2:
                self.num += 1
                if self.num >= self.Count:
                    self.num += 0
                    game_framework.pop_state()
            else:
                self.min_counter = True
        elif stage1_state.on == 4:
            self.min_counter = False
        elif stage1_state.on == 5:
            self.min_counter = False
        elif stage1_state.on == 6:
            self.min_counter = False

        for i in range(0, self.num):
            if self.X[i] >=200:
                self.X[i] =5000
            else:
                self.X[i] += 10
                for j in range(self.num,self.Count):
                    self.Y[j] -=10

        if self.min_counter == True:
            self.min_time =0 #######################시간감소, 중복입력 방지 구현
            Main_Stage.min_time = self.min_time

    def handle_event(self,event):
        pass
    def draw(self):
        for j ,i in enumerate(self.Y):
                if self.color[j] ==0:
                #R
                    self.image.clip_draw(0, 0, 198, 200, 630+self.X[j], 100 + i+self.start)
                if self.color[j]==1:
                #B
                    self.image.clip_draw(203, 0, 200, 200, 630+self.X[j], 100 + i+self.start)
                if self.color[j]==2:
                #G
                    self.image.clip_draw(407, 0, 200, 200, 630-self.X[j], 100 + i+self.start)

