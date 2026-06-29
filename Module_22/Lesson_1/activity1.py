# import library
# initialize it 
# declare width height
# create a pygame surface
# add caption
# add game loop

import pygame # library

pygame.init() # initilalize the library so that we can we have access to all its functions

width, height = 500, 500

screen = pygame.display.set_mode((width, height)) # pygame screen of 500 x 500

pygame.display.set_caption('My Game Window')


# game loop is a continuous loop that runs while the game is active

while True: 
    # list of events
    for event in pygame.event.get(): # Quit, enter, escaped
        if event.type == pygame.QUIT:
            pygame.quit() # quit from the game

    screen.fill((255,0,0)) # red
    pygame.display.flip() 

