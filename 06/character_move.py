from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')




def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('Circle')

    cx , cy, r = 400, 300, 200

    
    for DG in range(270,270 + 360, 5):
        
        x = cx + r * math.cos(DG / 360 * 2 * math.pi)
        y = cy + r * math.sin(DG / 360 * 2 * math.pi)
        render_all(x,y)
      


def run_rectangle():
    print('Rectangle')

    
    for x in range(50 , 750 +1 ,10):
        render_all(x,90)

    for y in range(90,550 + 1,10):
        render_all(750,y)

    for x in range(750, 50 - 1, -10):
       render_all(x , 550)

    for y in range(550,90 - 1,-10):
       render_all(50,y)

   


while True:
    run_circle()
    run_rectangle()
    break



    
close_canvas()
