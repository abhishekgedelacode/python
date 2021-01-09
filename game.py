import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('gameName')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    gameDisplay.fill((0, 0, 0))

    pygame.display.update()

pygame.quit()
quit()
