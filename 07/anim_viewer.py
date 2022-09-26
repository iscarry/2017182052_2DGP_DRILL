from pico2d import *

open_canvas(900, 640)
grass = load_image('grass.png')
character = load_image('pngwing01.com.png')
character02 = load_image('pngwing.com02.png')
character03 = load_image('pngwing.com03.png')
character04 = load_image('pngwing.com04.png')

running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

while running:
    frame = 0
    frame2 = 0
    frame3 = 0
    frame4 = 0
    x = 500

    while x > 450 and running:
        clear_canvas()
        grass.draw(450, 30)
        character03.clip_draw(frame3 * 90, 0, 80, 90, x, 90)
        update_canvas()

        handle_events()
        frame3 = (frame3 + 1) % 4
        x -= 5
        delay(0.1)

    while running:
        clear_canvas()
        grass.draw(450, 30)
        character.clip_draw(frame * 90, 0, 80, 100, 450, 90)
        if frame == 6:
            break
        frame = (frame + 1) % 7

        update_canvas()
        delay(0.1)

    while running:
        clear_canvas()
        grass.draw(450, 30)
        character02.clip_draw(frame2 * 90, 0, 80, 100, 450, 90)
        if frame2 == 7:
            break
        frame2 = (frame2 + 1) % 8

        update_canvas()
        delay(0.1)

    while running:
        clear_canvas()
        grass.draw(450, 30)
        character04.clip_draw(frame4 * 90, 0, 80, 110, 450, 90)
        if frame4 == 7:
            break
        frame4 = (frame4 + 1) % 8

        update_canvas()
        delay(0.1)

    handle_events()

close_canvas()

