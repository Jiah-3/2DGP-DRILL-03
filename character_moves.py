from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 20
y = 90
X = 400
Y = 90
shape = 0
while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(shape == 0):
        if(x < 780 and y == 90):
            x += 5
            delay(0.01)
        elif(y < 560 and x == 780):
            y += 5
            delay(0.01)
        elif(y == 560 and x > 20):
            x -= 5
            delay(0.01)
        elif(y > 90 and x == 20):
            y -= 5
            delay(0.01)
        if(x == 20 and y == 90):
            shape = 1
    elif(shape == 1):
        if(x < 780 and y == 90):
            x += 5
            delay(0.01)
        elif(x > 400 and y < 560):
            x -= 5
            y += 470 / 76.0
            delay(0.01)
        elif(x > 20 and y > 90):
            x -= 5
            y -= 470 / 76.0
            delay(0.01)
        if(x == 20 and y > 89 or x == 20 and y < 91):
            shape = 2
    elif(shape == 2):
        for degree in range(-90, 270, 5):
            x = X + 250 * math.cos(math.radians(degree))
            y = Y + 250 * math.sin(math.radians(degree))+250
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            delay(0.01)
        shape = 0
        x = 20
        y = 90