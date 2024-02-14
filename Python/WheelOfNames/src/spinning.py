class Spinning:
    
    def __init__(self, init_angle):
        self.init_angle = init_angle
        self.time = 0 
        
    def spin(self):
        self.init_angle = (-1 * ((self.time-4.47)**2)) + 20
        self.time += 1/60
        
        
        return self.init_angle