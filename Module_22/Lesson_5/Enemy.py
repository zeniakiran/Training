import pygame
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_START_Y_MAX, ENEMY_START_Y_MIN, ENEMY_SPEED_X, ENEMY_SPEED_Y
pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyImg):
        super().__init__()
        self.image = enemyImg
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX) #(50,150)
        self.speed_x = ENEMY_SPEED_X
        self.speed_y = ENEMY_SPEED_Y

    # Move the enemy on the screen
    def update(self):
        # Move enemy 
        # x = 100 + 4 = 104
        self.rect.x += self.speed_x

        # Bounce from sides and move down
        # If enemy was moving right (+4), it now moves left (-4).
        # First reverse direction
        # Seconldy, move 20 steps down
        
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.speed_x *= -1 # 6 * -1 = -6
            self.rect.y += self.speed_y # y = 200 + 20
