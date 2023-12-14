import pygame


class Controller:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background_width, self.backgroud_height = self.screen.get_size()
        self.font_size = 30
        self.custom_font = pygame.font.Font('WheelOfNames/assets/font.ttf', self.font_size)
           
    def mainloop(self):
        running = True
        while running:
            
            for event in pygame.event.get():
                pass

            self.state = "MENU"

            while True:
                if self.state == "MENU":
                    self.menuLoop()
                elif self.state == "GAME":
                    self.spinLoop()
                elif self.state =="END":
                    self.endLoop()
    def menuLoop(self):
        
        font = pygame.font.Font(None, 36) 
        input_text = ""
        texty = 0
        self.screen.fill("black")
        
        while self.state == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_text = ''
                        texty += self.backgroud_height/30 
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                if event.type == pygame.QUIT:
                        pygame.quit()

            
            text_surface = self.custom_font.render(input_text, True, "white")
            self.screen.blit(text_surface, ((4 * self.background_width)/5,texty))
            pygame.display.flip()
        pass
    
    def spinLoop(self):
        pass
        
    def endLoop(self):
        pass