import game_framework
import pico2d

import menu_state
import game_state
import stage1_state
import stage2_state
import stage3_state
import stage4_state
pico2d.open_canvas(1200, 800, sync=True)
game_framework.run(menu_state)

pico2d.close_canvas()