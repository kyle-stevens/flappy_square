import random
import pygame
from pygame.locals import *

class Obstacle():
    position_x = 1000
    position_y = 0
    rect = None
    height = 0
    passed = False
    def __init__(self):
        self.position_x = 1000
        self.position_y = random.randint(0,1)
        self.height = random.randint(100, 250)
        if self.position_y == 0:
            self.position_y = 50
        else:
            self.position_y = 550-self.height

        self.rect = Rect((self.position_x, self.position_y), (50, self.height))


    def update_pos(self, round):
        max_speed = 10
        speed = 5

        speed = 5+round*0.005
        if speed > max_speed:
            speed = max_speed
        self.position_x -= speed
        self.rect = Rect((self.position_x, self.position_y), (50, self.height))
        #print(speed)
        return self.rect
