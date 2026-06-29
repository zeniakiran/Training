import pygame
import random

# Initialize Pygame
pygame.init()

# Define basic colors using pygame.Color
# Background colors

colors = {
  'blue' : pygame.Color('blue'),
  'light_blue' : pygame.Color('lightblue'),
  'dark_blue' : pygame.Color('darkblue'),
  'yellow' : pygame.Color('yellow'),
  'magenta' : pygame.Color('magenta'),
  'orange' : pygame.Color('orange'),
  'white' : pygame.Color('white'),
  'black' : pygame.Color('black')
}

screen_width, screen_height = 500, 500
bg_color = colors['black']

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Boundary Sprite")

# Set the initial background color
bg_color = colors['blue']
screen.fill(bg_color)

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE = pygame.USEREVENT + 1
BG_COLOR_CHANGE = pygame.USEREVENT + 2


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

  # Constructor method
  def __init__(self, color, height, width):
    # Call to the parent class (Sprite) constructor
    super().__init__()

    # Create the sprite's surface with dimensions and color
    self.image = pygame.Surface([width, height])
    self.image.fill(color)

    # Get the sprite's rect defining its position and size
    self.rect = self.image.get_rect()

    print("SELF RECT______", self.rect)

    # velocity tells how much and in what direction your sprite moves every frame.
    # self.velocity = [3, 2]
    # Move 3 pixels to the right→ (x-direction)
    # Move 2 pixels down → (y-direction)

    # Set initial velocity with random direction
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

  # Method to update the sprite's position
  def update(self):
    # Move the sprite by its velocity
    self.rect.x = self.rect.x + self.velocity[0]
    self.rect.y = self.rect.y + self.velocity[1]


    # Flag to track if the sprite hits a boundary
    boundary_hit = False

    # Check for collision with left or right boundaries and reverse direction
    if self.rect.left == 0 or self.rect.right == (screen_width -1):
      self.velocity[0] = -self.velocity[0]
      boundary_hit = True
    # Check for collision with top or bottom boundaries and reverse direction
    if self.rect.top == 0 or self.rect.bottom == (screen_height -1):
      self.velocity[1] = -self.velocity[1]
      boundary_hit = True

    # If a boundary was hit, post events to change colors
    if boundary_hit:
        self.change_color()
        change_background_color()
        # create event objects
        sp_color_change_evnt = pygame.event.Event(SPRITE_COLOR_CHANGE)
        bg_color_change_evnt = pygame.event.Event(BG_COLOR_CHANGE)

        # triggering/posting the event
        pygame.event.post(sp_color_change_evnt)
        pygame.event.post(bg_color_change_evnt)

  # Method to change the sprite's color
  def change_color(self):
    self.image.fill(random.choice([colors['yellow'], colors['magenta'], 
                                   colors['orange'], colors['white']]))


# Function to change the background color
def change_background_color():
  global bg_color
  bg_color = random.choice([colors['blue'], colors['light_blue'], colors['dark_blue']])


# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()

# Instantiate the sprite
sp_width, sp_height = 20, 30
sp1 = Sprite(colors['white'], sp_width, sp_height)

# Randomly position the sprite
sp1.rect.x = random.randint(0, (screen_width - sp_width))
sp1.rect.y = random.randint(0, (screen_height - sp_height))

# Add the sprite to the group
all_sprites_list.add(sp1)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE:
      sp1.change_color()
    #If the background color change event is triggered, change the background color
    elif event.type == BG_COLOR_CHANGE:
      change_background_color()

  # Update all sprites
  all_sprites_list.update()
  # Fill the screen with the current background color
  screen.fill(bg_color)
  # Draw all sprites to the screen
  all_sprites_list.draw(screen)

  # Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()