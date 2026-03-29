import pygame
import sys
from sprites import Snake
from utility import get_asset_path

pygame.init()

SCREEN_W = 600
SCREEN_H = 400
FPS = 60

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(FPS)