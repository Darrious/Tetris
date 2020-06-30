
import pygame


# Global vars
block_size = 20
screen_x = 400
screen_y = 500
fps = 30
shape_perm = [[]]

def draw_shape(x, y):
    shape_l1 = []
    shape_l1.append(pygame.Rect(x, y, 20, 20))
    shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
    shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
    shape_l1.append(pygame.Rect(x + 20, y-40, 20, 20))

    return shape_l1

def draw_grid(screen):
    for x in range(screen_x):
        for y in range(screen_y):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)




def game_loop():
    pygame.init()
    screen = pygame.display.set_mode([screen_x, screen_y])
    running = True

    orange = (240, 120, 40)

  
    lead_x = 220
    lead_y = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x -= 20

                if event.key == pygame.K_RIGHT:
                    lead_x += 20
        

        shape = draw_shape(lead_x, lead_y)
        #draw_grid(screen)
        screen.fill((0, 0, 0))
           
        for i in range(4):
            pygame.draw.rect(screen, orange, shape[i])

        if lead_y < screen_y - 20:
            lead_y += 20
        else:
            print("end")
            shape_perm.append(shape)
            lead_y = 0
            lead_x = 220

          
        #print(shape)  
        #print(shape_perm)
        

        pygame.display.flip()
        clock.tick(fps)



def main():
    game_loop()

main()
