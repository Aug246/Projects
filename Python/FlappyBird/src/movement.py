import pygame

class Movement:
    def __init__(self, x , y, img = None, t=0):
        """
        intializes the variables neccesary to process the moving objects positions
        args: surface: the intializes screen the program is drawn to, img: the image that is being moves, x=0(int): the initial x position of the image, y=0(int): the initial y position of the image
        """
        
        self.x = x
        self.y = y
        self.image = img
        self.t = t
    def pipeMove(self):
        """
        moves the pipes to the left at a constant speed

        """
        pipe_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - pipe_shift
        return self.x
    
    def backgroundMove(self):
        """
        moves the background to the left at constant speed. if it is completely of the screen it gets moves back to the right side
        """
        screen_width = self.image.get_size()[0]
        back_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - back_shift
        
        if abs(self.x) > screen_width:
            self.x = screen_width - 10 
        return self.x
    
    def birdJump(self):
        """
        uses a physics position formula to determine the birds y position as it rises and falls
        """
        self.y = self.y -(25*self.t)+ ((1/2) * (80) * ((self.t) ** 2))
        return self.y
    
    def birdFall(self):
        """
        after the bird falls a certain distance it no longer accelerates and falls linearly. the rate at which is falls is determines by this function
        """
        self.y = self.y + 10
        return self.y
    
    def birdSpeed(self):
        """
        takes the derivatve of the birdJump formula do determine the bird's velocity. if the self.speed is negative it is rising, if its postitive it is falling
        """
        self.speed = -25+ (80*self.t)
        return self.speed

    def groundMove(self):
        """
        moves the ground to the left at constant speed. if it is completely of the screen it gets moves back to the right side
        """
        image_width = self.image.get_size()[0]
        ground_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - ground_shift
        
        if abs(self.x) > image_width:
            self.x = image_width 
        return self.x
