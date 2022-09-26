from pico2d import *

open_canvas(900, 640)
character = load_image('pngwing01.com.png')
character02 = load_image('pngwing.com02.png')

running = True
x = 50
frame = 0
frame2 = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while running:
    clear_canvas()
    character.clip_draw(frame * 90, 0, 80, 100, 150, 300)
    frame = (frame + 1) % 6
    character02.clip_draw(frame * 90, 0, 80, 100, 300, 300)
    frame2 = (frame2 + 1) % 7

    update_canvas()
    handle_events()

    delay(0.1)

close_canvas()

