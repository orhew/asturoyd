import sys
import pygame
from ship import *
from pygame.locals import *
import random

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_h * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (25, 5, 30)
screen.fill(color)

# df = pd.read_csv('game_info.csv')

Asteroids = pygame.sprite.Group()
NumLevels = 4
Level = 1
# LevelData = df.iloc[level]
AsteroidCount = 3
Player = Ship((20, 200))


def main():
    global Level

    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = -10
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 10
            if event.key == pygame.K_UP:
                Player.speed[1] = -10
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = 0
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 0
            if event.key == pygame.K_UP:
                Player.speed[1] = 0
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 0
            Player.update()

        screen.fill(color)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
