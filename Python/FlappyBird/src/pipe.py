import pygame 

class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        """
        intializes the variables neccesary to draw the pipe on the screen and makes the bird a sprite
        args: args: surface: the intializes screen the program is drawn to, imgpath(str): the location to the image in the files, x=0(int): the initial x position of the pipe, y=0(int): the initial y position of the pipe
        """
        self.imgpath = imgpath
        image = pygame.image.load(self.imgpath)
        og_width, og_height = image.get_size()
        
        self.image = pygame.transform.scale(image, (og_width/3, og_height/3))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.surface = surface
        self.mask = pygame.mask.from_surface(self.image)
   
    def drawPipe(self):
        """
        blits the pipe onto the screen
        """
        self.surface.blit(self.image, (self.rect.x, self.rect.y))