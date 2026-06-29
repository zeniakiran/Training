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

# game loop is a continuous loop that runs while the game is active

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # .blit() method is used to draw one image (or surface) onto another surface
    screen.blit(backgroundImg, (0,0)) # x, y coordinates i.e, where to draw image
    screen.blit(birdImg, birdRect)
    pygame.display.flip()








