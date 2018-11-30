from pico2d import *

import game_framework
import menu_state
time_time=100
min_time=0
plus_time=0
class Stage:
    def __init__(self):
        self.image = load_image('game_sprite\\main_background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)

class Item:
    def __init__(self):
        self.image = load_image('game_sprite\\sprite.png')

    def update(self):
        pass

    def draw(self):
        #yellow
        self.image.clip_draw(0, 200, 80, 100, 200, 400)
        #green
        self.image.clip_draw(110, 200, 80, 100, 400, 400)
        #red
        self.image.clip_draw(220, 200, 80, 100, 600, 400)
        #blue
        self.image.clip_draw(0, 115, 80, 90, 800, 425)
        #self.image.draw(100, 000)

class Princess:
    def __init__(self):
        self.image = load_image('game_sprite\\sprite.png')
        self.image2 = load_image('game_sprite\\Rope.png')
        self.image3 = load_image('game_sprite\\help2.png')
        self.timer=get_time()
        self.y=0
        self.frame=0
    def update(self):
        global time_time
        self.timer2 =get_time()
        if self.timer2-self.timer >1.03:
            self.timer = get_time()
            self.timer2 = get_time()

        self.frame = (self.frame+ int(self.timer2-self.timer))%4
        if time_time <= 0:
            self.y+=1
            if self.y >= 250:
                game_framework.quit()
                self.y = 250
    def draw(self):
        global time_time
        if time_time <=0:
            self.image.clip_draw(110, 0, 85, 120, 1120, 200-self.y)
        else:
            self.image2.draw(1100, 450)
            self.image2.draw(1100, 350)
            self.image.clip_draw(0, 0, 85, 115, 1120, 200)
            self.image3.clip_draw(int(self.frame)*88, 0, 80, 100, 1160, 280)

class Time:
    def __init__(self):
        self.image = load_image('game_sprite\\main_background.png')
        self.timer =0
        self.font = load_font('ENCR10B.TTF', 60)
        self.main_time =100

        self.timer2=100
    def update(self):
        global time_time,min_time,plus_time
        self.timer =int(get_time())
        self.main_time = self.timer2 - self.timer-min_time + menu_state.menu_time +plus_time
        time_time = self.main_time
        if self.main_time ==0:
            game_framework.quit()
    def draw(self):
        self.font.draw(1060, 670, '%3d' % self.main_time, (255, 0, 0))

class Coin:
    def __init__(self, count=0):
        self.image = load_image('game_sprite\\sprite.png')
        self.count=count
    def update(self):
        pass
    def draw(self):

        if self.count >=1:
            self.image.clip_draw(220, 140, 50, 50, 720, 750)
            if self.count >= 2:
                self.image.clip_draw(220, 140, 50, 50, 770, 750)
                if self.count>= 3:
                    self.image.clip_draw(220, 140, 50, 50, 820, 750)
                    if self.count== 4:
                         self.image.clip_draw(220, 140, 50, 50, 870, 750)
