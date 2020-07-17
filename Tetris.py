
import pygame
import random

# Global vars
block_size = 20
fps = 5

screen_x = 200
screen_y = 400

shape_perm = []
perm_color = []
orange = (240, 120, 40)
purple = (110, 0, 250)
yellow = (250, 250, 0)
blue = (0, 25, 250)
red = (200, 20, 30)
green = (5, 175, 15)
cyan = (50, 200, 200)

def shape_picker():
    return random.randint(1, 7)

def draw_shape(x, y, current_shape, rotation):
    shape_l1 = []
    global color
    # W shape
    if (current_shape == 1):
        color = purple
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 40, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))

        if (rotation == 1):
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y+20, 20, 20))
            shape_l1.append(pygame.Rect(x + 40, y, 20, 20))

        if (rotation == 2):
            shape_l1.append(pygame.Rect(x+20, y+20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 40, y, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))

        if (rotation == 3):
            shape_l1.append(pygame.Rect(x+20, y+20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))

    
    # reverse L
    if (current_shape == 2):
        color = orange
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-40, 20, 20))
        
        if (rotation == 1):

            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 40, y, 20, 20))
        
        if (rotation == 2):
            shape_l1.append(pygame.Rect(x+40, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        
        if (rotation == 3):
            shape_l1.append(pygame.Rect(x+40, y, 20, 20))
            shape_l1.append(pygame.Rect(x+40, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
    
    # I shape
    if (current_shape == 3):
        color = cyan
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x, y-60, 20, 20))
        if (rotation == 1):
            print(x, y)
            y -=20
            shape_l1.append(pygame.Rect(x+40, y, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y, 20, 20))
        if (rotation == 2):
            shape_l1.append(pygame.Rect(x+20, y, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-60, 20, 20))
        if (rotation == 3):
            shape_l1.append(pygame.Rect(x+40, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-40, 20, 20))
    
    # O shape
    if (current_shape == 4):
        color = yellow
        shape_l1.append(pygame.Rect(x, y, 20, 20))
        shape_l1.append(pygame.Rect(x, y-20, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
   
    # Z shape
    if (current_shape == 5):
        color = red
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-20, 20, 20))

        if (rotation == 1):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
        if (rotation == 2):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-20, 20, 20))

        if (rotation == 3):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))

    # S shape
    if (current_shape == 6):
        color = green
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
        if (rotation == 1):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-40, 20, 20))
        if (rotation == 2):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
        if (rotation == 3):
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x-20, y-40, 20, 20))
    
    # L
    if (current_shape == 7):
        color = blue
        if (rotation == 0):
            shape_l1.append(pygame.Rect(x+40, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-40, 20, 20))
        
        if (rotation == 1):

            shape_l1.append(pygame.Rect(x, y+20, 20, 20))
            shape_l1.append(pygame.Rect(x, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
            shape_l1.append(pygame.Rect(x + 40, y, 20, 20))
        
        if (rotation == 2):
            shape_l1.append(pygame.Rect(x, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x + 20, y, 20, 20))
        
        if (rotation == 3):
            shape_l1.append(pygame.Rect(x+40, y-40, 20, 20))
            shape_l1.append(pygame.Rect(x+40, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x+20, y-20, 20, 20))
            shape_l1.append(pygame.Rect(x, y-20, 20, 20))
    
    return shape_l1

def line_clear(shape_y, perm_y, perm_color):
    count = 0
    y_val = 0
    index = []
    color_index = []
    
   
    for i in perm_y:
        if i[1] == screen_y - 20:
            count+=1
    print(count)
    if (count == 10):    
        print("line clear")
        for i in range(len(perm_y)):
            for j in range(len(perm_y[i])):
                if(perm_y[i][j] == screen_y - 20):
                    index.append(perm_y[i])
                    color_index.append(perm_color[i])

        
        for i in index:
            perm_y.remove(i)
        for i in color_index:
            perm_color.remove(i)
        
        print(perm_y)
        for i in range(len(perm_y)):
            if (perm_y[i][1] == screen_y - 20):
                perm_y[i] = (perm_y[i][0], (perm_y[i][1] - 20))
        print(perm_y)
        

            

    return perm_y



#Checks for collision of blocks with edges of screen
def bound_check(shape):
    for i in shape:
        if (i[0] + 20 == 200) or (i[0] - 20 == -20):
            return True


    return False

#Checks for collision of blocks with each other
def collision_check(shape, perm):
    shape_y = []
    perm_y = []
    y_check = False
    x_check = False
    b_check = False

    for i in range(len(shape)):
        shape_y.append((shape[i][0],shape[i][1]))

    for i in range(len(perm)):
           perm_y.append((perm[i][0], perm[i][1]))

    b_check = bound_check(shape_y)
    
   
    # check block collision
    for i in shape_y:
        for j in perm_y:
            #y cord check
            if i[0] == j[0]:
                if((i[1] + 25) > j[1]):
                    y_check = True
                    break

            #x cord check
            if i[1] == j[1]:
                if((i[0] + 20) == j[0] or (i[0] + 20) == 350):
                    x_check = True
                if((i[0] - 20) == j[0] or (i[0] - 20) == 250):
                    x_check = True
        if(i[1] == 380):
            y_check = True
            break
                  
            
            
    return y_check, x_check, b_check


def draw_grid(screen):
    for x in range(screen_x):
        for y in range(screen_y):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)



def game_loop():
    global fps
    pygame.init()
    screen = pygame.display.set_mode([screen_x, screen_y])
    running = True
    current_shape = shape_picker()
    rotation = 0
   
    start_x = 80
    start_y = 0
    clock = pygame.time.Clock()

    while running:
        shape = draw_shape(start_x, start_y, current_shape, rotation)
        coll_check = collision_check(shape, shape_perm)
        line_clear(shape, shape_perm, perm_color)
        

        # These listen for arrow key pushes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (not coll_check[2]):
                    start_x -= 20

                if (event.key == pygame.K_RIGHT) and (not coll_check[2]):
                    start_x += 20
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP):
                    if (rotation == 3):
                        rotation = 0
                    else:
                        rotation+=1
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN):   
                    if (rotation == 0):
                        rotation = 3
                    else:
                        rotation-=1

        
        #draw_grid(screen)
        screen.fill((0, 0, 0))
           

        # Drawing shape
        for i in range(len(shape)):
            pygame.draw.rect(screen, color, shape[i])
        
        
        # Checking for a block collision
        if(coll_check[0]):
            #print("end")
            for i in range(len(shape)):
                shape_perm.append(shape[i])
                perm_color.append(color)

            start_y = 0
            start_x = 80
            current_shape = shape_picker()
            rotation = 0

        start_y += 20
        


        # Drawing stored blocks
        for i in range(len(shape_perm)):
            pygame.draw.rect(screen, perm_color[i], shape_perm[i])
        
        pygame.display.flip()
        clock.tick(fps)
    
        
def main():
    game_loop()

main()
