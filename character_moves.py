from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 20
y = 90
while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(x < 780 and y == 90):
        x += 2
        delay(0.01)
    elif(y < 560 and x == 780):
        y += 2
        delay(0.01)