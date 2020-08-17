
import pygame
import random

# Global vars
block_size = 20
fps = 8

screen_x = 200
screen_y = 400
screen_x_bord = 275


shape_perm = []
perm_color = []
orange = (240, 120, 40)
purple = (110, 0, 250)
yellow = (250, 250, 0)
blue = (0, 25, 250)
red = (200, 20, 30)
green = (5, 175, 15)
cyan = (50, 200, 200)
grey = (40, 40, 40)

# Picks a random shape
def shape_picker():
    return random.randint(1, 7)

def draw_shape(x, y, current_shape, rotation, next_shape):
    shape_l1 = []
    next_prev = []
    next_col = (0, 0, 0)
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
       
    
    # L shape
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
    
    # The below code is for displaying the preview for the next block
    prev_size = 10
    if(next_shape==1):
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(250, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 30, prev_size, prev_size))
        next_col = purple


    if(next_shape==2):   
        next_prev.append(pygame.Rect(230, 20, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(220, 40, prev_size, prev_size))
        next_col = yellow


    if(next_shape==3):     
        next_prev.append(pygame.Rect(230, 10, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 20, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_col = cyan


    if(next_shape==4):     
        next_prev.append(pygame.Rect(230, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 40, prev_size, prev_size))
        next_col = yellow


    if(next_shape==5):     
        next_prev.append(pygame.Rect(240, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(220, 30, prev_size, prev_size))
        next_col = red


    if(next_shape==6):     
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(250, 30, prev_size, prev_size))
        next_col = green


    if(next_shape==7):     
        next_prev.append(pygame.Rect(230, 20, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 30, prev_size, prev_size))
        next_prev.append(pygame.Rect(230, 40, prev_size, prev_size))
        next_prev.append(pygame.Rect(240, 40, prev_size, prev_size))
        next_col = blue

    return shape_l1, next_prev, next_col

def line_clear(shape_y, perm_y, perm_color):
    count = 0
    y_val = 0
    index = []
    line_val = -20
    line_pos = 0
    check = False

    while line_val > -380:
        count = 0
        for i in perm_y:
            if i[0][1] == screen_y + line_val:
                count+=1 # This variable tracks how many blocks are on a line

        #if there are 10 blocks on the row, delete it
        index = []
        if (count >= 10):    
            print("line clear")
            for i in range(len(perm_y)):
                for j in range(len(perm_y[i])):
                    if(perm_y[i][0][j] == screen_y + line_val):
                        index.append(perm_y[i])
                        
            

            for i in index:
                i[0][0] += 20
                i[0][1] += 20
            
            # Removes the line from the perm array and color array
            for i in index:
                perm_y.remove(i)
                print(i)
                 
            # Moves blocks down after line clear
            for i in range(len(perm_y)): 
                if(perm_y[i][0][1] <= screen_y + line_val):
                    perm_y[i][0][1] = perm_y[i][0][1] + 20                     
            
        line_val=line_val - 20
        line_pos+=1
    


    return perm_y



#Checks for collision of blocks with edges of screen
def bound_check_l(shape):
    for i in shape:
        #print("Shape x:", i[0])
        if (i[0] - 20 == -20):
            return True


    return False


#Checks for collision of blocks with edges of screen
def bound_check_r(shape):
    for i in shape:
        #print("Shape x:", i[0])
        if (i[0] + 20 == 200):
            return True


    return False


# Shows a "faded" preview of where the block will drio
def shape_preview(shape, perm):
    shape_orig = shape
    while(not (collision_check(shape, perm)[0])):
        for i in shape:
            i[1] +=20

    return shape, shape_orig


#Checks for collision of blocks with each other
def collision_check(shape, perm):
    shape_y = []
    perm_y = []
    y_check = False
    x_check = False
    b_check_l = False
    b_check_r = False
    
    for i in range(len(shape)):
        shape_y.append((shape[i][0],shape[i][1]))

    for i in range(len(perm)):
           perm_y.append((perm[i][0][0], perm[i][0][1]))
    
    # These variables check for left or right bound checks (The screen borders)
    b_check_l = bound_check_l(shape_y)
    b_check_r = bound_check_r(shape_y)
    
   
    # check block collision
    for i in shape_y:
        for j in perm_y:
            #y cord check
            if i[0] == j[0]:
                if((i[1] + 25) > j[1]):
                    y_check = True
                    break

            #x cord check (checks if another block is to the left or right)
            if i[1] == j[1]:
                if((i[0] + 20) == j[0] or (i[0] + 20) == 350):
                    x_check = True
                if((i[0] - 20) == j[0] or (i[0] - 20) == 250):
                    x_check = True
        if(i[1] == 380):
            y_check = True
            break
                  
            
            
    return y_check, x_check, b_check_l, b_check_r

# This draws a background grid
def draw_grid(screen):
    for x in range(screen_x):
        for y in range(screen_y):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)



def game_loop():
    global fps
    
    pygame.init()
    
    #Setting up variables
    screen = pygame.display.set_mode([screen_x_bord, screen_y])
    running = True
    current_shape = shape_picker()
    next_shape = shape_picker()
    rotation = 0
   
    start_x = 80
    start_y = 0
    clock = pygame.time.Clock()
    count = 0
    frame = 0
    frame_control = 9

    
    #Draw right border background
    pygame.draw.rect(screen, grey,(50,50,50,400))

    
    # The game loop
    while running:
        count = (count + 1) % 2

        shape = draw_shape(start_x, start_y, current_shape, rotation, next_shape)[0]
        next_prev = draw_shape(start_x, start_y, current_shape, rotation, next_shape)[1]
        next_col =  draw_shape(start_x, start_y, current_shape, rotation, next_shape)[2]
        coll_check = collision_check(shape, shape_perm)
        
        # Check for line clears
        line_clear(shape, shape_perm, perm_color)
        line_clear(shape, shape_perm, perm_color)
        line_clear(shape, shape_perm, perm_color)
        line_clear(shape, shape_perm, perm_color)
  

        # These listen for key pushes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (not coll_check[2]):
                    start_x -= 20
                    coll_check = collision_check(shape, shape_perm)


                if (event.key == pygame.K_RIGHT) and (not coll_check[3]) and (not coll_check[1]):
                    start_x += 20
                    coll_check = collision_check(shape, shape_perm)

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_v):
                    if (rotation == 3):
                        rotation = 0
                    else:
                        rotation+=1
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_c):   
                    if (rotation == 0):
                        rotation = 3
                    else:
                        rotation-=1
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN):   
                    fps = 1_000_000

        
        #Fill background
        screen.fill((0, 0, 0))
        #draw_grid(screen)
        pygame.draw.rect(screen, grey,(200,0, screen_x_bord-200, screen_y))
        
        

        # Displays the next block preview
        for i in range(len(next_prev)):
            pygame.draw.rect(screen, next_col, next_prev[i])

        # Drawing shape and shap drop preview
        for i in range(len(shape)):
            pygame.draw.rect(screen, color, shape[i])
        shape = shape_preview(shape, shape_perm)
        shape_pre = shape[0]
        for i in range(len(shape_pre)):
            pygame.draw.rect(screen, grey, shape_pre[i])
        shape = shape[1]
        
        # Checking for a block collision
        if(coll_check[0]):
            for i in range(len(shape)):
                shape_perm.append((shape[i], color));
               

            start_y = 0
            start_x = 80
            current_shape = next_shape
            next_shape = shape_picker()
            rotation = 0
            fps = 8
            #if(frame_control > 1):
                #frame_control -= 0.25
        
        # We use this to control the speed of block fall
        frame +=1
        if(frame % frame_control == 0):
            start_y += 20
        


        # Drawing stored blocks (blocks that have been dropped)
        for i in range(len(shape_perm)):
            pygame.draw.rect(screen, shape_perm[i][1], shape_perm[i][0])     
            if(shape_perm[i][0][1] <= 0):
            	#print(shape_perm[i])
            	print("game lost")
            	running = False
            
        
        pygame.display.flip()
        clock.tick(fps)


    
        
def main():
    game_loop()

main()



