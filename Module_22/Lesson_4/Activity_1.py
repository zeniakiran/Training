import pygame
import random

# Constants for easier adjustments
MOVEMENT_SPEED = 5 # move 5 pixels per frame
FONT_SIZE = 72

screen_width, screen_height = 500, 400

# Initialize Pygame
pygame.init()

# Load and transform the background image
# scale, rotate, flip, etc
# 1900 x 1080 px
background_image = pygame.transform.scale(pygame.image.load("background.jpeg"),
                                          (screen_width, screen_height))

# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    # constructor method 
    # first one to be called when any new obj is created
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(color))  # Background color of sprite

        # get the position of our rectangle
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change): 
        self.rect.x += x_change
        self.rect.x = min(max(0,self.rect.x), screen_width - self.rect.width) 

        self.rect.y += y_change
        self.rect.y = min(max(0,self.rect.y), screen_height - self.rect.height) 


# Setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision")

# creating a sprite group
all_sprites = pygame.sprite.Group()

# Create sprites
sprite_width, sprite_height = 20, 30
sprite1 = Sprite(pygame.Color('black'), sprite_width, sprite_height)

# randomly selecting x & y values everytime
# x = random.randint(0, 450) 
sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y =random.randint(0, screen_height - sprite1.rect.height)

all_sprites.add(sprite1)
    
sprite2 = Sprite(pygame.Color('red'), sprite_width, sprite_height)

sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)

all_sprites.add(sprite2)

# Game loop control variables
running, won = True, False
clock = pygame.time.Clock()

# Main game loop
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()

        x_change = 0
        y_change = 0
        
        # 0 + 5 = 5
        # 0 - 5 = -5
        # x_change = MOVEMENT_SPEED
        
        if keys[pygame.K_RIGHT]:
            x_change += MOVEMENT_SPEED
        if keys[pygame.K_LEFT]:
            x_change -= MOVEMENT_SPEED
        if keys[pygame.K_DOWN]:
            y_change += MOVEMENT_SPEED
        if keys[pygame.K_UP]:
            y_change -= MOVEMENT_SPEED

        sprite1.move(x_change, y_change)
        
        # colliderect() method is used to check if two rectangles
        # are colliding (overlapping) with each other
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        # screen.blit(thing to draw, where to draw)
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2,
                               (screen_height - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
