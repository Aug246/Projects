import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        """
        intializes the variables neccesary to draw the bird on the screen and makes the bird a sprite
        args: args: surface: the intializes screen the program is drawn to, imgpath(str): the location to the image in the files, x=0(int): the initial x position of the bird, y=0(int): the initial y position of the bird
        """
        self.imgpath = str(imgpath)
        self.surface = surface
        self.rotation_angle = 0

        
        image = pygame.image.load(self.imgpath)
        image_width, image_height = image.get_size()    
            
        self.image = pygame.transform.scale(image, (image_width/10, image_height/10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.mask = pygame.mask.from_surface(self.image)
    
    def drawBird(self):
        """
        blits and unrotated bird onto the screen
        """
        self.surface.blit(self.image, (self.rect.x, self.rect.y)) 
    
    def drawJumpBird(self):
        """
        blits the bird onto the screen and rotates it by a given angle
        """
       
        self.rotated_image = pygame.transform.rotate(self.image, self.rotation_angle)
        self.surface.blit(self.rotated_image, (self.rect.x, self.rect.y))
        
        
        