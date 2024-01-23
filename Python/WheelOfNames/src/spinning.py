class Spinning:
    
    def __init__(self, init_angle):
        self.init_angle = init_angle
        self.time = 0 
        
    def spin(self):
        self.init_angle = (-1 * ((self.time-3.16)**2)) +10
        
        
        return self.init_angle