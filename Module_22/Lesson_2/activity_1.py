# import library
# initialize it 
# declare width height
# create a pygame surface
# add caption
# add game loop

import pygame # library

pygame.init() # initilalize the library so that we can we have access to all its functions

width, height = 500, 500 # size of window

screen = pygame.display.set_mode((width, height)) # pygame screen of 500 x 500

pygame.display.set_caption('My Game Window')

# create a font
font = pygame.font.SysFont('Arial', 24) 
# antialiasing - it smoothes out the edges

# Render the text
text_surface = font.render("I am a Rectangle!", True, (255,255,255))

# Get the rectangle of the text surface and center it 
text_rect = text_surface.get_rect(center = (width // 2,30) )

# create rectangle and position in center
rect_width, rect_height = 60, 50
rectangle = pygame.Rect(0, 0, rect_width, rect_height)
rectangle.center= (width // 2, height // 2)

# game loop is a continuous loop that runs while the game is active

while True: 
    # list of events
    for event in pygame.event.get(): # Quit, enter, escaped
        if event.type == pygame.QUIT:
            pygame.quit() # quit from the game

    # copies pixel by pixel one surface to another
    screen.blit(text_surface, text_rect)
    pygame.draw.rect(screen, (255,0,0), rectangle) # (x, y, width, height)

    #screen.fill((0,0,0))
    pygame.display.flip() # to reflect the changes

    # copy the text surface on screen 
    
