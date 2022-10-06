import pygame
import os
import sys
import random
from time import sleep

# 정의
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)

FPS = 60

#클레스
class BattleShip(pygame.sprite.Sprite):
    def __init__(self):
        super(BattleShip, self).__init__()
        self.image = pygame.image.load('Battleship.png')
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = (SCREEN_WIDTH * 0.4)
        self.rect.y = (SCREEN_HEIGHT * 0.8)
        self.dx = 0
        self.dy = 0
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x < 0 or self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.rect.y -= self.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def colide(self):
        pass



class Fire(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Fire, self).__init__()
        self.image = pygame.image.load('Fire.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

    def colide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()
        self.rock01 = pygame.image.load('Rock01.png')
        self.G_rock = pygame.image.load('G_Rock.png')
        self.U_Rock = pygame.image.load('unique_rock.png')

        self.image = random.randint(1, 3)
        if self.image == 1:
            self.image = self.rock01
        elif self.image == 2:
            self.image = self.U_Rock
        else:
            if random.randint(1, 10) == 1:
                self.image = self.G_rock
            else:
                self.image = self.rock01

        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed



    def update(self):
        self.rect.y += self.speed

    def Count_miss_rock(self):
        if self.rect.y > SCREEN_HEIGHT:
            return True
class Game():
    def __init__(self):
        self.background_image = pygame.image.load('background.png')
        self.battleship = BattleShip()
        self.fires = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()

        self.count_miss = 0
        self.destroied_rock = 0
        self.default_font = pygame.font.Font('dist', 28)
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.battleship.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.battleship.dx += 5
                elif event.key == pygame.K_UP:
                    self.battleship.dy -= 5
                elif event.key == pygame.K_DOWN:
                    self.battleship.dy += 5
                elif event.key == pygame.K_SPACE:
                    fire = Fire(self.battleship.rect.centerx, self.battleship.rect.y, 10)
                    self.fires.add(fire)
                elif event.key == pygame.K_ESCAPE:
                    return True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.battleship.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.battleship.dy = 0


        return False

    def game_logic(self, screen):
        Ocur_Rock = 1
        Rock_Speed = 1
        Max_Speed = 2

        if random.randint(1, 60) == 1:
            for i in range(Ocur_Rock):
                speed = random.randint(Rock_Speed, Max_Speed)
                rock = Rock(random.randint(30, SCREEN_WIDTH - 30), 0, speed)
                self.rocks.add(rock)

        for fire in self.fires:
            rock = fire.colide(self.rocks)
            if rock:
                self.destroied_rock += 1
                fire.kill()
                rock.kill()

        for rock in self.rocks:
            if rock.Count_miss_rock():
                rock.kill()
                self.count_miss += 1



    def display_frame(self, screen):

        screen.blit(self.background_image, self.background_image.get_rect())
        self.draw_text(screen, 'Destroyed Meteorite:{}'.format(self.destroied_rock), self.default_font, 100, 20, YELLOW)
        self.rocks.update()
        self.rocks.draw(screen)
        self.fires.update()
        self.fires.draw(screen)
        self.battleship.update()
        self.battleship.draw(screen)

    def draw_text(self, screen, text, front, x, y, color):
        text_obj = pygame.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)


def main():
    pygame.init()
    pygame.display.set_caption('Space_Guardian')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False

    while not done:

        done = game.process_events()


        game.game_logic(screen)
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()



