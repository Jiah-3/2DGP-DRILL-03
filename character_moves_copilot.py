from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rectangle():
    margin = 20
    start_x, start_y = 20, 90
    max_y = 540
    points = [
        (start_x, start_y),
        (800 - margin, start_y),
        (800 - margin, max_y),
        (margin, max_y)
    ]
    for i in range(4):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%4]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)

def move_triangle():
    margin = 20
    start_x, start_y = 20, 90
    max_y = 540
    points = [
        (start_x, start_y),
        (700, start_y),
        (400, max_y)
    ]
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%3]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)

def move_circle():
    # 원 궤적 (중심: 400, 315 / 반지름: 225)
    cx, cy, r = 400, (90 + 540) // 2, (540 - 90) // 2
    for deg in range(0, 360, 2):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
