from pico2d import *
import game_framework
from Boy import Boy
from Grass import Grass

boy = None
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)

# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN:
#             match event.key:
#                 case pico2d.SDLK_ESCAPE:
#                     game_framework.quit()
#                 case pico2d.SDLK_LEFT:
#                     boy.dir -= 1
#                 case pico2d.SDLK_RIGHT:
#                     boy.dir += 1
#         elif event.type == SDL_KEYUP:
#             match event.key:
#                 case pico2d.SDLK_LEFT:
#                     boy.dir += 1
#                     boy.face_dir = -1
#                 case pico2d.SDLK_RIGHT:
#                     boy.dir -= 1
#                     boy.face_dir = 1

# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
