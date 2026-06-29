import pygame # import pygame

pygame.init() # initialize pygame to access all its functions

width, height = 500, 500

# display functions
# set mode
# set caption
# flip
# update
# get caption
# set icon

screen = pygame.display.set_mode((width, height)) # create a display window

pygame.display.set_caption("My Fun Game Window") # set window caption

backgroundImg = pygame.transform.scale(pygame.image.load('birthday.jpeg').convert(), (width, height))
birdImg = pygame.transform.scale(pygame.image.load('bird.jpeg').convert_alpha(), (200, 200))
birdRect = birdImg.get_rect(center = (width // 2, height // 2))
print(birdRect)

# game loop code

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(backgroundImg, (0,0))
    screen.blit(birdImg, birdRect)
    #screen.fill((255,255,255))
    pygame.display.flip()

    # code below will run till flag is false








