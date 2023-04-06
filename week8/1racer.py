import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Racer")

FPS = pygame.time.Clock()
FPS.tick(60)
running = True

while running:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



