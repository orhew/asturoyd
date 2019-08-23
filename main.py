import random
import sys
import matplotlib.pyplot as plt
import pandas as pd
from pygame.locals import *

from asteroid import Asteroid
from ship import *

pygame.init()
screen = pygame.display.Info()

size = (width, height) = (int(screen.current_w * 0.5), int(screen.current_h * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (25, 5, 30)
screen.fill(color)

df = pd.read_csv('game_info.csv')

Asteroids = pygame.sprite.Group()
NumLevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData['AsteroidCount']
Player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))
Deaths = 0
TotalDeaths = []


def init():
    global AsteroidCount, Asteroids, Deaths, TotalDeaths

    LevelData = df.iloc[Level]
    Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))
    Asteroids.empty()
    AsteroidCount = LevelData['AsteroidCount']
    for i in range(AsteroidCount):
        Asteroids.add(Asteroid((random.randint(50, width - 50), random.randint(50, height - 50)), random.randint(15, 60)))
    Deaths = 1

def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Escaped!!", True, (0, 0, 255))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    font2 = pygame.font.SysFont(None, 40)
    text2 = font2.render("Deaths: {}".format(str(Deaths))), True, (0, 0, 255)
    text2_rect = text2.get_rect()
    text2_rect.center = (width / 2, height / 2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        screen.blit(text2, text2_rect)
        pygame.display.flip()

    Index = np.arange(len(TotalDeaths))
    plt.bar(Index, TotalDeaths)
    plt.xlabel('Level Number', fontsize=20)
    plt.ylabel('No. of tries', fontsize=20)
    plt.xticks(index, TotalDeaths, fontsize=20, rotation=5)
    plt.title('Tries per level')
    plt.show


def main():
    global Level, Deaths, TotalDeaths
    init()

    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 10
            if event.key == pygame.K_LEFT:
                Player.speed[0] = -10
            if event.key == pygame.K_UP:
                Player.speed[1] = -10
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.speed[0] = 0
            if event.key == pygame.K_LEFT:
                Player.speed[0] = 0
            if event.key == pygame.K_UP:
                Player.speed[1] = 0
            if event.key == pygame.K_DOWN:
                Player.speed[1] = 0

        Player.update()
        screen.fill(color)
        Asteroids.update()
        get_hits = pygame.sprite.spritecollide(Player, Asteroids, False)
        Asteroids.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()

        if Player.checkReset(width):
            TotalDeaths.append(Deaths)
            if Level == NumLevels:
                break
            else:
                Level += 1
                init()

        elif get_hits:
            Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))
            Deaths += 1
    win()


if __name__ == '__main__':
    main()
