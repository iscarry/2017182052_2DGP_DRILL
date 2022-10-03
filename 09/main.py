import random
from pico2d import *


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global sx, sy
    global ax, ay, t

    t = 0
    ax, ay = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    sx, sy = x, y
    pass


def update_world():
    global x, y
    global t
    t += 0.005
    x = (1-t) * sx + t * ax
    y = (1-t) * sy + t * ay

    if t >= 1.0:
        reset_world()
    pass




TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
sx = TUK_WIDTH / 2
sy = TUK_HEIGHT / 2
x, y = sx, sx
ax, ay = x, y
t = 0
frame = 0
hide_cursor()


reset_world()

while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(ax, ay)
    if x < ax:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)


    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
