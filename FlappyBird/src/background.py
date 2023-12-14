import pygame

class Background:
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        """
        Initializes the necessary variables to draw the background on the screen
        args: surface: the intializes screen the program is drawn to, imgpath(str): the location to the image in the files, x=0(int): the initial x position of the background, y=0(int): the initial y position of the background 
        """
        self.x = x
        self.y = y
        self.imgpath = str(imgpath)
        self.surface = surface
        self.image = pygame.image.load(self.imgpath)
    def drawBackground(self):
        """
        blits the background onto the screen
        """
        self.surface.blit(self.image, (self.x, self.y))
