
import pygame
import random

# Global vars
block_size = 20
fps = 13

screen_x = 400
screen_y = 500

shape_perm = []
perm_color = []
orange = (240, 120, 40)
purple = (110, 0, 250)
yellow = (250, 250, 0)
blue = (0, 25, 250)

def shape_picker():
	return random.randint(1, 4)

def draw_shape(x, y, current_shape):
    shape_l1 = []
    global color
    # W shape
    if (current_shape == 1):
        color = purple
        shape_l1.append(pygame.Rect(x, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 40, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
    
    # L shape 1
    if (current_shape == 2):
        color = orange
        shape_l1.append(pygame.Rect(x, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y-40, 20, 20))
    
    # I shape
    if (current_shape == 3):
        color = blue
        shape_l1.append(pygame.Rect(x, y, 20, 20))
        shape_l1.append(pygame.Rect(x, y-20, 20, 20))
        shape_l1.append(pygame.Rect(x, y-40, 20, 20))
        shape_l1.append(pygame.Rect(x, y-60, 20, 20))
    
    # O shape
    if (current_shape == 4):
        color = yellow
        shape_l1.append(pygame.Rect(x, y, 20, 20))
        shape_l1.append(pygame.Rect(x, y-20, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))

    return shape_l1

def collision_check(shape, perm):
    shape_y = []
    perm_y = []

    for i in range(len(shape)):
        shape_y.append((shape[i][0],shape[i][1]))

    for i in range(len(perm)):
           perm_y.append((perm[i][0], perm[i][1]))



    #print("Shape:",shape_y)
    #print("Perm:",perm_y)
    y_check = False
    x_check = False
    # check
    for i in shape_y:
        for j in perm_y:
        	#y cord check
            if i[0] == j[0]:
                if((i[1] + 25) > j[1]):
                    y_check = True
                    break

            #x cord check
            if i[1] == j[1]:
                if((i[0] + 20) == j[0]):
            	    print("right lock")
            	    x_check = True
                if((i[0] - 20) == j[0]):
                    x_check = True
                    print("left lock")

    
    return y_check, x_check


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
    current_shape = random.randint(1,4)

    
  
    lead_x = 200
    lead_y = 0
    clock = pygame.time.Clock()

    while running:
        shape = draw_shape(lead_x, lead_y, current_shape)
        check = collision_check(shape, shape_perm)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (not check[1]):
                    lead_x -= 20

                if (event.key == pygame.K_RIGHT) and (not check[1]):
                    lead_x += 20
        

        
        #draw_grid(screen)
        screen.fill((0, 0, 0))
           
        for i in range(len(shape)):
            pygame.draw.rect(screen, color, shape[i])
        
        
        if(check[0]):
            #print("end")
            for i in range(len(shape)):
                   shape_perm.append(shape[i])
                   perm_color.append(color)

            lead_y = 0
            lead_x = 200
            current_shape = shape_picker()

        if lead_y < screen_y - 20:
            lead_y += 20
        else:
            print("end")

            for i in range(len(shape)):
                shape_perm.append(shape[i])
                perm_color.append(color)

            lead_y = 0
            lead_x = 200
            current_shape = shape_picker()


        
        for i in range(len(shape_perm)):

            pygame.draw.rect(screen, perm_color[i], shape_perm[i])
        

        pygame.display.flip()
        clock.tick(fps)
        
def main():
    game_loop()

main()
