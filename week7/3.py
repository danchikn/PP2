import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

Red = (255, 0, 0)
White = (255, 255, 255)

color = Red
x, y = 25, 25
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        if x < 465:
            x += 20
    elif pressed[pygame.K_LEFT]:
        if x > 35:
            x -= 20
    elif pressed[pygame.K_DOWN]:
        if y < 465:
            y += 20
    elif pressed[pygame.K_UP]:
        if y > 35:
            y -= 20

    screen.fill(White)
    pygame.draw.circle(screen, color, [x, y], 25, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

"""
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("moving")

x = 200
y = 200

width = 20
height = 20

velocity = 10

running = True

while running:
    pygame.time.delay(10)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += velocity

    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += velocity

    screen.fill((21, 60, 226))
    pygame.draw.circle (screen, (199,62,62), (x,y), 25, 0)

pygame.quit()
"""

