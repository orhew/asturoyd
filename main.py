import sys
import pygame
import random

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (30, 0, 30)
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
            screen.fill(color)
            screen.blit(Player.image, Player.rect)
            pygame.display.flip()


if __name__ == '__main__':
    main()