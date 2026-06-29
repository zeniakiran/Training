# import library
# initialize it 
# declare width height
# create a pygame surface
# add caption
# add game loop

# i need a rectangle 
# i need to add boundaries for my rectangle
# I need my rectangle to move around
# i wanto to change its color whenit touches any boundary


import pygame # library

pygame.init() # initilalize the library so that we can we have access to all its functions


# declare needed variables

def move_rectangle(): 
    width, height = 500, 500 # screen width, height

    colors = {
        'red' : pygame.Color('red'),
        'green' : pygame.Color('green'),
        'blue' : pygame.Color('blue'),
        'yellow' : pygame.Color('yellow')

    }

    keys = {
        'left' : pygame.K_LEFT, 
        'right' : pygame.K_RIGHT, 
        'up' : pygame.K_UP,
        'down' : pygame.K_DOWN
    }

    #keys['right'] = 255

    current_color = pygame.Color('white')

    rect_width, rect_height = 50, 50
    # 500 - 50 = 450 // 2 =  225 

    # get the perfect center
    x = (width - rect_width) // 2 
    y = (height - rect_height) // 2

    # pygame screen of 500 x 500
    screen = pygame.display.set_mode((width, height)) 

    # set window title
    pygame.display.set_caption('My Game Window')

    # game loop is a continuous loop that runs while the game is active
    running = True
    while running: 
        # list of events
        for event in pygame.event.get(): # Quit, enter, escaped
            if event.type == pygame.QUIT:
                running = False

        # get the pressed key
        # 1- if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE:
                #print("Space key pressed!")

        keyPressed = pygame.key.get_pressed() 

        #(0, 0) ----------------> x increases →
    #|
    #|
    #|
    # ↓ y increases 
    # 50 - 1 = 49

        if keyPressed[keys['up']]: # keyPressed['up']
            y = y-1

        if keyPressed[keys['down']]:
            y = y+1

        if keyPressed[keys['left']]:
            x = x-1

        if keyPressed[keys['right']]:
            x = x+1

        # prevent from going outside boundaries
        # (0,-600)
        # min(460, 450)
        # 450 
                # max(0,-100)
        x = min(max(0,x), width - rect_width) # (430, 450)
        y = min(max(0,y), height - rect_height)

        rectangle = pygame.Rect(x, y, rect_width, rect_height)

        screen.fill((0, 0, 0)) # clearing the screen 

        if x == 0:
            current_color = colors['blue']
        elif x == width - rect_width: # 500-50 = 450
            current_color = colors['red']
        elif y == 0:
            current_color = colors['green']
        elif y == height - rect_height:
            current_color = colors['yellow']

        
        pygame.draw.rect(screen, current_color, rectangle)

        pygame.display.flip() 

    print("OUTSIDE LOOP")
    pygame.quit() # quit from the game


if __name__ == '__main__':
    move_rectangle()