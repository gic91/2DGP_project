from pico2d import *

import menu_world
import game_framework



# fill expressions correctly
PIXEL_PER_METER =(10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RAD = PIXEL_PER_METER *3
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 8


UP_UP,UP_DOWN, DOWN_UP,DOWN_DOWN ,SPACE= range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACE
}

# Boy States

class StartState:

    @staticmethod
    def enter(menu, event):
        menu.timer =0

    @staticmethod
    def exit(menu, event):
        if event ==SPACE:
            menu.start =1
    @staticmethod
    def do(menu):
        menu.timer +=1
    @staticmethod
    def draw(menu):
        if menu.timer % 50 >=20:
            menu.image.draw(600, 400)
        else :
            menu.image2.draw(600,400)


class TutoState:

    @staticmethod
    def enter(menu, event):
        menu.timer = 0

    @staticmethod
    def exit(menu, event):
        pass
    @staticmethod
    def do(menu):
        menu.timer += 1

    @staticmethod
    def draw(menu):
        if menu.timer % 50 >=30:
            menu.image.draw(600, 400)
        else :
            menu.image3.draw(600,400)


class ExitState:

    @staticmethod
    def enter(menu, event):
        menu.timer = 0

    @staticmethod
    def exit(menu, event):
        if event == SPACE:
            game_framework.quit()

    @staticmethod
    def do(menu):
        menu.timer += 1

    @staticmethod
    def draw(menu):
        if menu.timer % 50 >= 30:
            menu.image.draw(600, 400)
        else:
            menu.image4.draw(600, 400)


next_state_table = {
    StartState: {UP_UP: StartState, DOWN_UP: StartState,
    DOWN_DOWN: TutoState, UP_DOWN: StartState, SPACE : StartState},

    TutoState: {UP_UP: TutoState, DOWN_UP: TutoState,
               UP_DOWN: StartState, DOWN_DOWN: ExitState ,SPACE : TutoState},

    ExitState: {UP_UP: ExitState, DOWN_DOWN: ExitState,
                 DOWN_UP: ExitState, UP_DOWN: TutoState,  SPACE : ExitState},


}

class Menu:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('game_sprite\\background_title.png')
        self.image2 = load_image('game_sprite\\background_title_1.png')
        self.image3 = load_image('game_sprite\\background_title_2.png')
        self.image4 = load_image('game_sprite\\background_title_3.png')
        self.start =0
        self.timer = 0
        self.timer2 = 0
        self.event_que = []
        self.cur_state = StartState
        self.cur_state.enter(self, None)
        self.sleep_on=0



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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

