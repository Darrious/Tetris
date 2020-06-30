
import pygame



pygame.init()
screen = pygame.display.set_mode([400, 500])

running = True
blockSize = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 100, 100))

    
    #drawGrid()
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(200, 200, 20, 20 ))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 200, 20, 20 ))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 220, 20, 20 ))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 240, 20, 20 ))
    pygame.display.update()


