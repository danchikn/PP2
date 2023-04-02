import pygame

pygame.init()

screen = pygame.display.set_mode((600,800))

running = True

songs = ['C://Users//Anar//Desktop//PP2//songs//eminem-mockingbird.mp3',
          'C://Users//Anar//Desktop/PP2//songs//Goblin 도깨비 OST (Chanyeol, Punch) - Stay with me MV (256  kbps).mp3',
          'C://Users//Anar//Desktop//PP2//songs//james-arthur-back-from-the-edge.mp3']

play = True
num = 0

font = pygame.font.SysFont("comicsansms", 30)

clock = pygame.time.Clock()
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

while running:
    current = num
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play
                elif event.key == pygame.K_RIGHT:
                    if num < len(songs) - 1:
                        num += 1
                    else:
                        num = 0
                elif event.key == pygame.K_LEFT:
                    if num > 0:
                        num -= 1
                    else:
                        num = len(songs) - 1

        screen.fill((0, 0, 0))

        name = songs[num].replace('musics/', '')
        name = name.replace('.mp3', '')

        text = font.render(name, True, (56, 87, 89))
        text_rect = text.get_rect(center=(600 / 2, 800 / 2))

        screen.blit(text, text_rect)

        if play == False:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        if (current != num):
            pygame.mixer.music.load(songs[num])
            pygame.mixer.music.play()

    pygame.display.flip()
    clock.tick(60)