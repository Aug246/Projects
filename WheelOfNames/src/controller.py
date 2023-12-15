import pygame


class Controller:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background_color = (48, 63, 89)
        self.textbox_color = (73, 96, 135)
        self.background_width, self.backgroud_height = self.screen.get_size()
        self.font_size = 30
        self.custom_font = pygame.font.Font('assets/font.ttf', self.font_size)
           
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
        
        input_text = ''
        textx , texty = (4 * self.background_width)/5, self.backgroud_height/3

        self.input_text_list = []
        self.screen.fill(self.background_color)
        text_box = pygame.draw.rect(self.screen, self.textbox_color, ((4 * self.background_width)/5 -10 , self.backgroud_height/3 - 10, self.background_width/5, (4*self.backgroud_height)/9))
        
        while self.state == "MENU":
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_RETURN:
                        
                        if len(self.input_text_list) < 10 and  input_text != '':
                            self.input_text_list.append(input_text)
                            input_text = ''
                            
                            texty += self.backgroud_height/25 
                            text_box.h -= self.backgroud_height/25
                        
                    elif event.key == pygame.K_BACKSPACE:
                        if input_text == '':
                            if len(self.input_text_list) > 0:
                                
                                texty -= self.backgroud_height/25
                                text_box.h += self.backgroud_height/25
                                input_text = self.input_text_list[-1]
                                self.input_text_list = self.input_text_list[:-1]
  
                                
                        elif input_text != "":        
                            input_text = input_text[:-1]         
                    else:
                        input_text += event.unicode
                        
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
            if len(self.input_text_list) >= 10:
                input_text = ""
                        
            

            pygame.draw.rect(self.screen, self.textbox_color,(textx - 10 , texty - 10 , text_box.w, text_box.h))
            text_surface = self.custom_font.render(input_text, True, "white")
            self.screen.blit(text_surface, (textx,texty))
            
            pygame.display.flip()

    
    def spinLoop(self):
        
        pass
        
    def endLoop(self):
        pass