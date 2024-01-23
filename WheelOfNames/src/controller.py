import pygame
import random
from src.slice import Slice
from src.spinning import Spinning

class Controller:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background_color = (48, 63, 89)
        self.screen.fill(self.background_color)
        self.background_width, self.backgroud_height = self.screen.get_size()
        
        self.textbox_color = (73, 96, 135)
        
        self.font_size = 30
        self.custom_font = pygame.font.Font('assets/font.ttf', self.font_size)
        
        self.slice = Slice(self.screen, self.background_width/2, self.backgroud_height/2)
        self.input_text_list = []
        self.textx , self.texty = (4 * self.background_width)/5, self.backgroud_height/3
           
    def mainloop(self):
        running = True
        self.text_box = pygame.draw.rect(self.screen, self.textbox_color, ((4 * self.background_width)/5 -10 , self.backgroud_height/3 - 10, self.background_width/5, (4*self.backgroud_height)/9))
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
        
        while self.state == "MENU":
            text_num = len(self.input_text_list)
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_RETURN:
                        
                        if text_num < 10 and  input_text != '':
                            self.input_text_list.append(input_text)
                            input_text = ''
                            
                            self.texty += self.backgroud_height/25 
                            self.text_box.h -= self.backgroud_height/25
                        
                    elif event.key == pygame.K_BACKSPACE:
                        if input_text == '':
                            if text_num > 0:
                                
                                self.texty -= self.backgroud_height/25
                                self.text_box.h += self.backgroud_height/25
                                input_text = self.input_text_list[-1]
                                self.input_text_list = self.input_text_list[:-1]
  
                                
                        elif input_text != "":        
                            input_text = input_text[:-1]         
                    else:
                        input_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if text_num > 0:
                        if play_button.collidepoint(event.pos):
                            self.state = "GAME"
                        else:
                            pass
                        
                elif event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                       
            if text_num >= 10:
                input_text = ""
            if text_num > 1:
                self.slice.slice_num = len(self.input_text_list)
            elif text_num <= 1:
                self.slice.slice_num = 1
     
            

            
            text_surface = self.custom_font.render(input_text, True, "white")
            pygame.draw.rect(self.screen, self.textbox_color,(self.textx - 10 , self.texty - 10 , self.text_box.w, self.text_box.h))
            self.screen.blit(text_surface, (self.textx,self.texty))
            
            self.slice.createSlices()
            pygame.draw.circle(self.screen, (207, 204, 205), (self.slice.center_x, self.slice.center_y), self.backgroud_height/14)
            
            play_button = pygame.draw.circle(self.screen, "white", (self.slice.center_x, self.slice.center_y), self.backgroud_height/14, int(self.backgroud_height/100))
            pygame.display.flip()

    
    def spinLoop(self):
        self.time = 0
        clock = pygame.time.Clock()
        while self.state == "GAME":
            spin = Spinning(self.slice.angle_degree)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
            angle_shift = (-1 * ((self.time-4.47)**2)) + 20
            self.slice.angle_degree += angle_shift
            self.time += 1/60
            self.slice.createSlices()
            
            if angle_shift <= 0:
                self.state = "END"
            
            pygame.display.flip()
            clock.tick(60) 


        
    def endLoop(self):
        
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
            angle_change = self.slice.angle_degree % 360
            x = angle_change/self.slice.slice_num
            y = 0
            
            for i in range(self.slice.slice_num):
                y += x
                if y > 270:
                    print(self.input_text_list[i])
                    self.state = "MENU"

        