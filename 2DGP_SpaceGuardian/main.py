from pico2d import*


# 정의
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT) # 스크린 정의

Battle_ship_image = load_image('Battleship.png')
Battle_ship_x = SCREEN_WIDTH / 2
Battle_ship_y = SCREEN_HEIGHT / 10
Battle_ship_dx = 0
Battle_ship_dy = 0



Fire_image = load_image('Fire.png')
Fire_x = 0
Fire_y = 0
Fire_speed = 10



Done = False  #게임의 진행상태 체크

#게임 반복 구간
while not Done:
    clear_canvas()

    #이벤트 반복구간
    for event in get_events():

        if event.type == SDL_QUIT: # 윈도우 종료시 반복 중지
            Done = True

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                Battle_ship_dx = -3
            elif event.key == SDLK_RIGHT:
                Battle_ship_dx = 3
            elif event.key == SDLK_UP:
                Battle_ship_dy = 3
            elif event.key == SDLK_DOWN:
                Battle_ship_dy = -3
            elif event.key == SDLK_SPACE:
                Fire_image.draw(Battle_ship_x, Battle_ship_y)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                Battle_ship_dx = 0
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                Battle_ship_dy = 0
    # 게임 로직

    Battle_ship_x += Battle_ship_dx
    Battle_ship_y += Battle_ship_dy


    #배경화면

    #회면 그리기
    Battle_ship_image.draw_now(Battle_ship_x, Battle_ship_y)

    # 회면 업데이트
    update_canvas()

    # 초당 60프레임 고정

    #delay(0.01)

# 게임 종료
close_canvas()




