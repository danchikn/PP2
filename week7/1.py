import pygame

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Play.com")
icon = pygame.image.load('../images/icon.p.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50,75))
square.fill((182,18,154))

myfon = pygame.font.Font('../Fons/Montserrat-ThinItalic.ttf', 20)
text_surface = myfon.render('Love u world, but not today', True, 'Purple', 'White')

player = pygame.image.load('../images/icon.p.png')

running = True
while running:

    screen.blit(square,(10,0))

    pygame.draw.circle(screen, 'Red', (10,7), 5)
    screen.blit(text_surface,(300,100))
    screen.blit(player,(50,20))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
