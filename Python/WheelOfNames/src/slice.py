import pygame
import math


class Slice:
    def __init__(self, surface, center_x = 0 , center_y = 0, slice_num = 0):
        
        self.surface = surface
        self.slice_num = slice_num
        self.center_x = center_x
        self.center_y = center_y
        self.color = (90, 92, 90)
        self.angle_degree = 0

        self.background_width = self.surface.get_size()[0]
        self.radius = self.background_width/4

        
    def createSlices(self):
        
        num_sides = int(11520/self.slice_num)
        angle_degree = self.angle_degree
        colors = [(51,105,232), (4,153,36), (238,179,19), (214,16,37)]
        index = 0 
        
        for _ in range(self.slice_num):
            self.color = colors[index]
            index = (index + 1) % len(colors)
            points = [(self.center_x, self.center_y)]
            
            for _ in range(num_sides):
                
                angle_rad = math.radians(angle_degree)
                
                x_point = self.center_x + (self.radius * math.cos(angle_rad))
                y_point = self.center_y + (self.radius * math.sin(angle_rad))
                
                points.append((x_point, y_point))
                
                angle_degree += 0.03125
            
            pygame.draw.polygon(self.surface, self.color, points)
            
            
        