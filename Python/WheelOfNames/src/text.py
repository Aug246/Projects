import math
import pygame

class Text:
    
    def __init__(self, surface, text_list, angle_shift, radius, centerx, centery, slice_angle):
        
        self.surface = surface
        self.text_list = text_list
        self.angle_shift = angle_shift
        self.radius = radius/2
        self.centerx = centerx
        self.centery = centery
        self.text_spacing = slice_angle
        
        self.font_size = 30
        self.custom_font = pygame.font.Font('assets/font.ttf', self.font_size)
        
    def displayText(self):
        
        def rotateText(text, x, y, angle):
            text_surface = self.custom_font.render(text, True, "white")
            rotated_surface = pygame.transform.rotate(text_surface, angle)
            rotated_rect = rotated_surface.get_rect()
            rotated_rect.center = (x, y)
            self.surface.blit(rotated_surface, rotated_rect)
        
        for i in range(len(self.text_list)):
                
                angle_rad = math.radians(self.angle_shift + (self.text_spacing/2))
                
                x_point = self.centerx + (self.radius * math.cos(angle_rad))
                y_point = self.centery + (self.radius * math.sin(angle_rad))
                
                rotateText(self.text_list[i], x_point, y_point, -1 * (self.angle_shift + (self.text_spacing/2)))
                
                self.angle_shift += self.text_spacing
                
        