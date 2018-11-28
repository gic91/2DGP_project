from pico2d import *

import game_framework
import random
import Main_Stage

time_time = Main_Stage.time_time


def makeshell(num,limit):
    while num <= limit:
        yield num
        num += 1
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
        self.image = load_image('game_sprite\\shell.png')
        self.Count =10
        self.Y=[]
        self.color=[1,0,0,2,0,1,2,0,1,2]
        for i in range(0,self.Count):
            #self.color.append(random.randint(0,2))
            self.Y.append(i*200)
        self.start=500
    def update(self):
        self.start-=10
        if self.start <=0:
            self.start =0
    def draw(self):
        for j ,i in enumerate(self.Y):
                if self.color[j] ==0:
                #R
                    self.image.clip_draw(0, 0, 198, 200, 630, 100 + i+self.start)
                if self.color[j]==1:
                #B
                    self.image.clip_draw(203, 0, 200, 200, 630, 100 + i+self.start)
                if self.color[j]==2:
                #G
                    self.image.clip_draw(407, 0, 200, 200, 630, 100 + i+self.start)

