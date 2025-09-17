from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

clear_canvas_now()
grass.draw_now(400, 30)
character.draw_now(20, 90)

delay(1)