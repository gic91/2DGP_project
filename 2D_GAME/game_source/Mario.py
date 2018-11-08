from pico2d import *

import math
import game_world
import game_framework
import stage1_state
import stage2_state
import stage3_state
import stage4_state
import random
from Main_Stage import Coin
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RAD = PIXEL_PER_METER * 3
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE,UP_DOWN= range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN
}


# Boy States
coin =None
box1 =False
box2=False
box3=False
box4=False
class IdleState:

    @staticmethod
    def enter(boy, event):
        global coin
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer2 = int(get_time())
        if boy.Coin_count ==4:
            if event == UP_DOWN:
                if boy.x > 920 and boy.x<1100:
                    game_framework.exit()
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.jump_on = True

    @staticmethod
    def do(boy):
        global coin,box1,box2,box3,box4

        boy.frame = (boy.frame + 0.5*FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        boy.timer = int(get_time())
        if boy.jump_on == True :
            if boy.jump_check == True:
                boy.jump -= 10
            elif boy.jump_check == False:
                boy.jump += 10
            if boy.jump >=200:
                boy.jump_check =True
                if boy.x >=170 and boy.x<=240:
                    if box1 ==False:
                        boy.Coin_count +=1
                        box1 =True
                        coin =Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage1_state)
                elif boy.x >=370 and boy.x<=440:

                    if box2 == False:
                        boy.Coin_count += 1
                        box2 = True
                        coin =Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage2_state)
                elif boy.x >=570 and boy.x<=640:

                    if box3 == False:
                        boy.Coin_count += 1
                        box3 = True
                        coin =Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage3_state)
                elif boy.x >=770 and boy.x<=840:

                    if box4 == False:
                        boy.Coin_count += 1
                        box4 = True
                        coin =Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage4_state)
            elif boy.jump <0:
                boy.jump_check = False
                boy.jump_on =False



    @staticmethod
    def draw(boy):
        if boy.Coin_count == 4:
            boy.image2.clip_draw(110, 140, 50, 50,boy.x, 50+boy.y + boy.jump)
        if boy.dir == 1:

            if int(boy.frame) == 0:
                boy.image.clip_draw(0, 365, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 1:
                boy.image.clip_draw(50, 365, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 2:
                boy.image.clip_draw(110, 365, 50, 90, boy.x,  boy.y + boy.jump)
            elif int(boy.frame) == 3:
                boy.image.clip_draw(225, 365, 60, 90, boy.x,  boy.y + boy.jump)
            elif int(boy.frame) == 4:
                boy.image.clip_draw(225, 365, 60, 90, boy.x,  boy.y + boy.jump)



        else:
            if int(boy.frame) == 0:
                boy.image.clip_draw(0, 275, 50, 90, boy.x,  boy.y + boy.jump)
            elif int(boy.frame) == 1:
                boy.image.clip_draw(50, 275, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 2:
                boy.image.clip_draw(110, 275, 50, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 3:
                boy.image.clip_draw(165, 275, 60, 90, boy.x, boy.y + boy.jump)
            elif int(boy.frame) == 4:
                boy.image.clip_draw(225, 275, 60, 90, boy.x, boy.y + boy.jump)


class RunState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)
        if boy.Coin_count ==4:
            if event == UP_DOWN:
                if boy.x > 920 and boy.x<1100:
                    game_framework.quit()
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.jump_on =True

    @staticmethod
    def do(boy):
        global coin, box1, box2, box3, box4
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %6
        boy.x += boy.velocity * game_framework.frame_time
        if boy.x > 1000:
            boy.x =1000
        elif boy.x <0:
            boy.x = 0
        boy.x = clamp(25, boy.x, 1600 - 25)
        if boy.jump_on == True:
            if boy.jump_check == True:
                boy.jump -= 10
            elif boy.jump_check == False:
                boy.jump += 10
            if boy.jump >= 200:
                boy.jump_check = True
                if boy.x >= 170 and boy.x <= 240:
                    if box1 == False:
                        boy.Coin_count += 1
                        box1 = True
                        coin = Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage1_state)
                elif boy.x >= 370 and boy.x <= 440:

                    if box2 == False:
                        boy.Coin_count += 1
                        box2 = True
                        coin = Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage2_state)
                elif boy.x >= 570 and boy.x <= 640:

                    if box3 == False:
                        boy.Coin_count += 1
                        box3 = True
                        coin = Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        boy.cur_state = IdleState
                        boy.dir = 1
                        boy.velocity = 0
                        game_framework.push_state(stage3_state)
                elif boy.x >= 770 and boy.x <= 840:

                    if box4 == False:
                        boy.Coin_count += 1
                        box4 = True
                        coin = Coin(boy.Coin_count)
                        game_world.add_object(coin, 0)
                        game_framework.push_state(stage4_state)
            elif boy.jump < 0:
                boy.jump_check = False
                boy.jump_on = False




    @staticmethod
    def draw(boy):
        if boy.Coin_count ==4:
            boy.image2.clip_draw(110, 140, 50, 50, boy.x, 50 + boy.y + boy.jump)
        if boy.dir == 1:
            if boy.jump_on ==True:
                boy.image.clip_draw(50, 0, 50, 95, boy.x, boy.y + boy.jump)
            else:
                if int(boy.frame) == 0:
                    boy.image.clip_draw(0, 180, 50, 95, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 1:
                    boy.image.clip_draw(50, 180, 50, 95, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 2:
                    boy.image.clip_draw(110, 180, 50, 95, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 3:
                    boy.image.clip_draw(165, 180, 60, 95, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 4:
                    boy.image.clip_draw(225, 180, 60, 95, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 5:
                    boy.image.clip_draw(285, 180, 60, 95, boy.x, boy.y+boy.jump)
        else:
            if boy.jump_on == True:
                boy.image.clip_draw(290, 0, 50, 95, boy.x, boy.y + boy.jump)
            else:
                if int(boy.frame) == 0:
                    boy.image.clip_draw(0, 92, 50, 90, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 1:
                    boy.image.clip_draw(50, 92, 50, 90, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 2:
                    boy.image.clip_draw(110, 92, 50, 90, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 3:
                    boy.image.clip_draw(170, 92, 60, 90, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 4:
                    boy.image.clip_draw(225, 92, 60, 90, boy.x, boy.y+boy.jump)
                elif int(boy.frame) == 5:
                    boy.image.clip_draw(285, 92, 60, 90, boy.x, boy.y+boy.jump)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,  SPACE: IdleState, UP_DOWN :IdleState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,  SPACE: RunState, UP_DOWN : RunState},


}


class Mario:

    def __init__(self):
        self.x, self.y = 50, 148
        self.image = load_image('game_sprite//Mario.png')
        self.image2 = load_image('game_sprite//sprite.png')
        self.dir = 1
        self.velocity = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame = 0
        self.timer = 0
        self.timer2 = 0
        self.stage = 0
        self.Coin_count=0
        self.jump_on = False
        self.jump =0
        self.jump_check = False
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.sleep_on = 0

    def get_bb(self):

        return self.x - 25, self.y - 40+self.jump, self.x + 25, self.y + 40+self.jump

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        #self.font.draw(self.x - 60, self.y + 50, '(Time:%3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
