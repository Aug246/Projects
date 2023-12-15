import pygame
import math

class Slice(pygame.sprite.Sprite):
    def __init__(self, surface, x,y, slice_num, position):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.slice_num = slice_num
        self.center = x,y
    def createSlices(self):
        
        num_sides = int(360/self.slice_num)
        points = [self.center]
        
        for n in range(num_sides):
            point0x = points[n][n]
            point0y = points[n][n+1]
            
        