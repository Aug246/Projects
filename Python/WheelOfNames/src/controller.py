import pygame
import random
from src.slice import Slice
from src.spinning import Spinning
from src.text import Text

class Controller:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background_color = (48, 63, 89)
        self.screen.fill(self.background_color)
        self.background_width, self.backgroud_height = self.screen.get_size()
        
        self.textbox_color = (73, 96, 135)
        
        self.font_size = 40
        self.custom_font = pygame.font.Font(None, self.font_size)
        
        self.slice = Slice(self.screen, self.background_width/2, self.backgroud_height/2)
        self.input_text_list = []
        self.textx , self.texty = (4 * self.background_width)/5, self.backgroud_height/3
           
    def mainloop(self):
        running = True
        #self.text_box = pygame.draw.rect(self.screen, self.textbox_color, ((4 * self.background_width)/5 -10 , self.backgroud_height/3 - 10, self.background_width/5, (4*self.backgroud_height)/9))
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
        self.screen.fill(self.background_color)
        self.text_box = pygame.draw.rect(self.screen, self.textbox_color, ((4 * self.background_width)/5 -10 , self.backgroud_height/3 - 10, self.background_width/5, (4*self.backgroud_height)/9))
        self.textx , self.texty = (4 * self.background_width)/5, self.backgroud_height/3
        input_text = ''
        
        for i in range(len(self.input_text_list)):
            if len(self.input_text_list)  == 0 :
                break

            text_surface = self.custom_font.render(self.input_text_list[i], True, "white")
            self.screen.blit(text_surface, (self.textx,self.texty))
            self.texty += self.backgroud_height/25 
            self.text_box.h -= self.backgroud_height/25

        
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
            pygame.draw.rect(self.screen, "White", (self.slice.center_x - self.background_width/100, self.slice.center_y - self.backgroud_height/2.1, self.background_width/50, self.backgroud_height/10))
            
            
            self.wheel_text = Text(self.screen, self.input_text_list, self.slice.angle_degree, self.slice.radius, self.slice.center_x, self.slice.center_y, 360/self.slice.slice_num)
            self.wheel_text.displayText()
            pygame.display.flip()      
    
    def spinLoop(self):
        clock = pygame.time.Clock()
        spin = Spinning(self.slice.angle_degree)

        while self.state == "GAME":
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
            angle_shift = spin.spin()
            self.slice.angle_degree += angle_shift
            self.wheel_text.angle_shift = self.slice.angle_degree
            self.slice.createSlices()
            self.wheel_text.displayText()
            
            if angle_shift <= 0:
                self.state = "END"
                
            pygame.draw.circle(self.screen, (207, 204, 205), (self.slice.center_x, self.slice.center_y), self.backgroud_height/14)
            
            play_button = pygame.draw.circle(self.screen, "white", (self.slice.center_x, self.slice.center_y), self.backgroud_height/14, int(self.backgroud_height/100))
            pygame.draw.rect(self.screen, "White", (self.slice.center_x - self.background_width/100, self.slice.center_y - self.backgroud_height/2.1, self.background_width/50, self.backgroud_height/10))
            
            pygame.display.flip()
            clock.tick(60) 

    def endLoop(self):
        clock = pygame.time.Clock()
        choice_boxwidth, choice_boxheight = 0, 0 
        condition_met = False
        confetti_fall = True
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_box.collidepoint(event.pos):
                            self.state = "MENU"
                            
            #uses the total degrees changed and % by 360 to find how far from the 0 degree it has moved           
            angle_change = self.slice.angle_degree % 360
            
            #source angle means how far back the origin has moved
            source_angle = angle_change - 360
            slice_angle = 360 / self.slice.slice_num
            
            #adds whatever the angle a slice takes everytime the for loop runs until it is bigger than 270 which is the slice that is selected
            
            while not condition_met:
                
                transparent_surface = pygame.Surface((self.background_width, self.backgroud_height), pygame.SRCALPHA)
                transparent_surface.fill((0, 0, 0, 128))
                self.screen.blit(transparent_surface, (0, 0))
                
                for i in range(self.slice.slice_num):
                    source_angle += slice_angle
                    if source_angle >= 270:
                        print(self.input_text_list[i])
                        decision = self.input_text_list[i]
                        condition_met = True
                        break
                      

            
            while choice_boxwidth < self.background_width/2:
                choice_boxwidth += self.background_width/10
                choice_boxheight += self.backgroud_height/12
                decision_box = pygame.draw.rect(self.screen, (73, 96, 135), (self.background_width/4 ,self.backgroud_height/4, choice_boxwidth, choice_boxheight))
                pygame.display.flip()
                clock.tick(60) 
                
            pygame.draw.rect(self.screen, (65, 79, 105), (decision_box.x, decision_box.y, decision_box.w, decision_box.h/9.8))   
            
            exit_box = pygame.draw.rect(self.screen, (100, 122, 161), (decision_box.x + decision_box.w * 0.95, decision_box.y + decision_box.h * 0.01, decision_box.h * 0.09, decision_box.h * 0.09))
            exit_box_bottomrightx, exit_box_bottomrighty = exit_box.bottomright
            pygame.draw.line(self.screen, "White", (exit_box.x + exit_box.w/6, exit_box.y + exit_box.h/6), (exit_box_bottomrightx - exit_box.w/6, exit_box_bottomrighty - exit_box.h/6), 5)
            pygame.draw.line(self.screen, "White", (exit_box.x + exit_box.w/6, exit_box.y + (5 * exit_box.h)/6), (exit_box.x + (5 * exit_box.w)/6, exit_box.y + exit_box.h/6), 5)
            
            decision_textfont = pygame.font.Font(None, 100)
            decision_text = decision_textfont.render(decision, True, "white")
            decision_text_width = decision_text.get_width()
            decision_text_height = decision_text.get_height()
            
            self.screen.blit(decision_text, (decision_box.centerx - decision_text_width/2 , decision_box.centery - decision_text_height/2))

                
            
            pygame.display.flip()

