
import pygame


# Global vars

def draw_grid(screen):
    blockSize = 20 #Set the size of the grid block
    for x in range(400):
        for y in range(500):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode([400, 500])

    running = True
    blockSize = 20

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        
        draw_grid(screen)
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(200, 200, 20, 20 ))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 200, 20, 20 ))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 220, 20, 20 ))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(220, 240, 20, 20 ))
        pygame.display.update()


def main():
	game_loop()

main()
