
import pygame


# Global vars
block_size = 20
shape_l1 = []
def draw_grid(screen):
    for x in range(400):
        for y in range(500):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)




def game_loop():
    pygame.init()
    screen = pygame.display.set_mode([400, 500])
    running = True

    orange = (240, 120, 40)

   
    lead_x = 220
    lead_y = 0
    clock = pygame.time.Clock()
    #lead_x_change = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_LEFT:
            		#lead_x_change = -20
            		lead_x -= 20
            	if event.key == pygame.K_RIGHT:
            		#lead_x_change = 20
            		lead_x += 20
        
        #lead_x += lead_x_change

        #draw_grid(screen)
        screen.fill((0, 0, 0))
       	pygame.draw.rect(screen, orange, [lead_x, lead_y, 20, 20 ])

       	if lead_y < 480:
            lead_y += 20
       

        pygame.display.flip()
        clock.tick(5)



def main():
	game_loop()

main()
