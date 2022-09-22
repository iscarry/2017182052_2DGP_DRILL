from pico2d import *
import math

open_canvas(800,600)

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
X = 180 / math.pi


while(x < 790):
    clear_canvas_now()
    
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x = x + 2
    delay(0.01)
    
while(y < 550):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y = y + 2
    delay(0.01)

while(x >= 0):
    clear_canvas_now()
    
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x = x - 2
    delay(0.01)

while(y >= 90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y = y - 2
    delay(0.01)    
    

while(x < 400):
    clear_canvas_now()
    
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x = x + 2
    delay(0.01)

while(X < 360):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400 + 300 * math.cos(X),300 + 300 * math.sin(X))
    X = X + 180 /math.pi
    delay(1)      


close_canvas()
