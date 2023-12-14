import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        super().__init__()
        """
        intializes the variables neccesary to draw the ground on the screen and makes the ground a sprite
        args: args: surface: the intializes screen the program is drawn to, imgpath(str): the location to the image in the files, x=0(int): the initial x position of the ground, y=0(int): the initial y position of the ground
        """
        self.imgpath = str(imgpath)
        self.surface = surface
        
        image = pygame.image.load(self.imgpath)
        og_height = image.get_size()[1]
        new_width= self.surface.get_size()[0]
        self.image = pygame.transform.scale(image, (new_width, og_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
    def drawGround(self):
        """
        blits the ground onto the screen
        """
        self.surface.blit(self.image, (self.rect.x, self.rect.y))