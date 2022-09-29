from pico2d import *


def colide():

    global x, y
    global dx, dy

    if x < 20 or x > TUK_WIDTH - 20:
        x -= dx * 5
    elif y < 20 or y > TUK_HEIGHT - 20:
        y -= dy * 5



def handle_events():
    global running
    global dx, dy
    global ani
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1
                ani = 1
            elif event.key == SDLK_LEFT:
                dx -= 1
                ani = 0
            elif event.key == SDLK_UP:
                dy += 1
            elif event.key == SDLK_DOWN:
                dy -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
            elif event.key == SDLK_LEFT:
                dx += 1
            elif event.key == SDLK_UP:
                dy -= 1
            elif event.key == SDLK_DOWN:
                dy += 1

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
x = TUK_WIDTH / 2
y = TUK_HEIGHT / 2
frame = 0
dx = 0
dy = 0
ani = 0

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH / 2, TUK_HEIGHT / 2)
    character.clip_draw(frame * 100, 100 * ani, 100, 100, x, y)
    update_canvas()


    handle_events()
    frame = (frame + 1) % 8
    x += dx * 5
    y += dy * 5
    colide()
    delay(0.01)

close_canvas()

