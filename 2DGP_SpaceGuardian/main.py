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

class BattleShip(pygame.sprite.Sprite):
    def __init__(self):
        super(BattleShip, self).__init__()
        self.image = pygame.image.load('Battleship.png')
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = int(SCREEN_WIDTH /2)
        self.rect.y = int(SCREEN_HEIGHT/10)
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

    def colide(self):
        pass


class Game():
    def __init__(self):
        self.background_image = pygame.image.load('background.png')
        self.battleship = BattleShip()
        self.fire = pygame.sprite.Group()

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
                    self.fire.add(fire)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.battleship.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.battleship.dy = 0


        return False


    def display_frame(self, screen):

        screen.blit(self.background_image, self.background_image.get_rect())
        self.fire.update()
        self.fire.draw(screen)
        self.battleship.update()
        self.battleship.draw(screen)


def main():
    pygame.init()
    pygame.display.set_caption('Space_Guardian')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False

    while not done:

        done = game.process_events()

        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()



