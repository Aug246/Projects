import pygame
import random
from src.background import Background
from src.movement import Movement
from src.ground import Ground
from src.pipe import Pipe
from src.bird import Bird


class Controller:

    def __init__(self):
        """
        initializes the pygame and the screen. also makes the sprite group for the pipes
        """
        pygame.init()
        self.screen = pygame.display.set_mode()
        
        self.bottompipes = pygame.sprite.Group()
    
    def mainloop(self):
        """
        Runs a loop that checks for the state of the program if it is in thhe menu game or end menu
        """

        running = True
        while running:
            
            for event in pygame.event.get():
                pass

            self.state = "MENU"

            while True:
                if self.state == "MENU":
                    self.menuloop()
                elif self.state == "GAME":
                    self.gameloop()
                elif self.state =="END":
                    self.endloop()
                      

    def menuloop(self):
        """
        Makes an interactive menu screen

        """
        clock = pygame.time.Clock()
          
        background1 = Background(self.screen, "assets/background.png")
        back1_move = Movement(background1.x, background1.y, background1.image)
        background_width, background_height = background1.image.get_size()
        background2 = Background(self.screen, "assets/background.png", background_width)
        back2_move = Movement(background2.x, background2.y, background2.image)
        
        ground1 = Ground(self.screen, "assets/ground.png", 0, background_height)
        ground1_move = Movement(ground1.rect.x, ground1.rect.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()        
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.rect.x, ground2.rect.y, ground2.image)
        
        
        play_buttonimg = pygame.image.load("assets/button.png")
        scaled_button = pygame.transform.scale(play_buttonimg, (background_width/6, ground_height))

        font_size = int(background_width/6)
        custom_font = pygame.font.Font('assets/FlappyBirdy.ttf', font_size)
        text = "Jumpy Birdy"
        
        border_width = 5

        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        
        bird = None
        bird_drawn = False
        menu_draw = True
        
        while self.state == "MENU" :
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        menu_draw = False

                        bird = Bird(self.screen, "assets/blueflappybird.png",background_width/3, background_height/2 )
                        bird_drawn = True
                    elif exit_button.collidepoint(event.pos):
                        pygame.quit()
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if bird:
                        bird.kill()
                        self.state = "GAME"
            
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.rect.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.rect.x = ground2_move.groundMove()
        
            if menu_draw == True:
                
                text_rendered = custom_font.render(text, True, "black")  
                self.screen.blit(text_rendered, (background_width/4, background_height/3))
                play_button = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/3) - 10 , (background_height + ground_height)/2, background_width/6, ground_height))
                border_play_button = pygame.draw.rect(self.screen, "black", (((background_width/3) - 10) - border_width , ((background_height + ground_height)/2)- border_width , (background_width/6) + (2* border_width), (ground_height) + (2* border_width)), border_width)

                exit_button = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/2) + 10, (background_height + ground_height)/2, background_width/6, ground_height))
                exit_button_border = pygame.draw.rect(self.screen, "black", (((background_width/2) + 10) - border_width , ((background_height + ground_height)/2) - border_width, (background_width/6) + (2* border_width), (ground_height)+ (2* border_width)), border_width)

                play_triangle_coords = [(play_button.x + play_button.width/4, play_button.y + play_button.height/6),(play_button.x + play_button.width/4, play_button.y + (2*play_button.width)/3),(play_button.x + (4*play_button.width)/5, play_button.y + play_button.height/2)]
                pygame.draw.polygon(self.screen, "green", play_triangle_coords)
                
                x_quit_coords = [(exit_button.x + exit_button.width/4, exit_button.y + exit_button.height/6),(exit_button.x + (4*exit_button.width)/5, exit_button.y + (2*exit_button.width)/3), (exit_button.x + exit_button.width/4, exit_button.y + (2*exit_button.width)/3), (exit_button.x + (4*exit_button.width)/5,exit_button.y + exit_button.height/6)]
                pygame.draw.line(self.screen, "red", x_quit_coords[0], x_quit_coords[1], 20)
                pygame.draw.line(self.screen, "red", x_quit_coords[2], x_quit_coords[3], 20 )
                
            if bird_drawn == True:    
                bird.drawBird()
                
            pygame.display.flip()
            clock.tick(60)  
        
    def gameloop(self):
        """
        makes and interactive game where you jump by presssing space and must navigate through obstavles
        """
        
        fall_counter = 0
        jump = True
        space_in_between = 200

        clock = pygame.time.Clock()

        background1 = Background(self.screen, "assets/background.png")
        back1_move = Movement(background1.x, background1.y, background1.image)
        background_width, background_height = background1.image.get_size()
        background2 = Background(self.screen, "assets/background.png", background_width)
        back2_move = Movement(background2.x, background2.y, background2.image)

        ground1 = Ground(self.screen, "assets/ground.png", 0, background_height)
        ground1_move = Movement(ground1.rect.x, ground1.rect.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()       
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.rect.x, ground2.rect.y, ground2.image)

        by = random.randint(int(((1/3)*(background_height))+35),int(background_height-35))
        bottompipe = Pipe(self.screen, "assets/bottompipe.png", background_width, by)
        self.bottompipes.add(bottompipe)
        b2y = random.randint(int(((1/3)*(background_height))+35),int(background_height-35))
        bottompipe2 = Pipe(self.screen, "assets/bottompipe.png", (background_width + (background_width)/2)-2 , b2y)
        self.bottompipes.add(bottompipe2)

        ty = by - space_in_between - bottompipe.image.get_size()[1]
        toppipe = Pipe(self.screen, "assets/toppipe.png", background_width, ty)
        self.bottompipes.add(toppipe)
        
        ty2 = b2y - space_in_between - bottompipe2.image.get_size()[1]
        toppipe2 = Pipe(self.screen, "assets/toppipe.png", (background_width + (background_width)/2)-2, ty2)
        self.bottompipes.add(toppipe2)

        game_bird = Bird(self.screen, "assets/blueflappybird.png",(background_width/3) , background_height/2 )
        bird_move = Movement(game_bird.rect.x, game_bird.rect.y)
        bird_move.t = 0

        font_size = int(background_width/8)
        custom_font = pygame.font.Font('assets/flappybirdnums.ttf', font_size)
        self.score_count = 0
        score = str(self.score_count)   
        score_write = False    


        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))

        
        while self.state == "GAME" :
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird_move.t = 0 

                    fall_counter = 0
                    jump = True

                elif event.type == pygame.QUIT:
                    pygame.quit()
            
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.rect.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.rect.x = ground2_move.groundMove()
            
            y = random.randint(int(((1/3)*(background_height))+35),int(background_height-35))
            for b in self.bottompipes:
                
                pipe_move = Movement(b.rect.x, b.rect.y)
                b.drawPipe()
                b.rect.x = pipe_move.pipeMove()   

                if b.rect.x < -100:

                    b.kill()
                    self.bottompipes.remove(b)
                    
                    space_in_between = 200
                    
                    if b.imgpath == "assets/bottompipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/bottompipe.png", background_width, y))
                    if b.imgpath == "assets/toppipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/toppipe.png", background_width, y - space_in_between - b.image.get_size()[1]))
                            
                if int(b.rect.x) == int(game_bird.rect.x):
                    self.score_count += 0.5
                    score = str(int(self.score_count)) 
                                        
            if pygame.sprite.spritecollide(game_bird, self.bottompipes, False, pygame.sprite.collide_mask):
                self.state = "END"
                score_write = True
                self.bottompipes.empty()
                  
            elif pygame.sprite.collide_rect(game_bird, ground1):
                self.state = "END"
                score_write = True
                self.bottompipes.empty()
            elif pygame.sprite.collide_rect(game_bird, ground2):
                self.state  = "END"
                score_write = True
                self.bottompipes.empty()
            bird_move.t += 1/40
            
            game_birdspeed = bird_move.birdSpeed()

            if jump:
                game_bird.rect.y = bird_move.birdJump()
                
            if int(game_birdspeed) > 0:
                fall_counter += 1/60      
                
                if fall_counter > 0.3:
                    jump = False
                    game_bird.rect.y = bird_move.birdFall()
                    game_bird.rotation_angle -= 7
                    
                    if game_bird.rotation_angle < -90:
                        game_bird.rotation_angle = -90  
                                    
            elif int(game_birdspeed) < 0:
                game_bird.rotation_angle += 20
                
                if game_bird.rotation_angle > 30:
                    game_bird.rotation_angle = 30
                    
            if score_write == True:
                score_text = open("etc/highscore.txt") 
                num_score = score_text.readline()
                score_text.close()
                
                if int(num_score) < self.score_count:   
                    highscore_set = open("etc/highscore.txt", 'w') 
                    highscore_set.write(score)
                    highscore_set.close()
                
            game_bird.drawJumpBird()
  
            text_rendered = custom_font.render(score, True, "black")  
            self.screen.blit(text_rendered, ((4*background_width)/9, background_height/12))
                  
            pygame.display.flip()
            clock.tick(60)
          
    def endloop(self):
        """
        creates an interactive end game menu, gives the score and current high score. 
        """
        clock = pygame.time.Clock()
        
        background1 = Background(self.screen, "assets/background.png")
        back1_move = Movement(background1.x, background1.y, background1.image)
        background_width, background_height = background1.image.get_size()
        background2 = Background(self.screen, "assets/background.png", background_width)
        back2_move = Movement(background2.x, background2.y, background2.image)

        ground1 = Ground(self.screen, "assets/ground.png", 0, background_height)
        ground1_move = Movement(ground1.rect.x, ground1.rect.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()       
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.rect.x, ground2.rect.y, ground2.image)
        
        play_buttonimg = pygame.image.load("assets/button.png")
        scaled_button = pygame.transform.scale(play_buttonimg, (background_width/6, ground_height))
        
        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        
        font_size = int(background_width/15)
        wordscore_font = pygame.font.Font('assets/FlappyBirdy.ttf', font_size)
        numscore_font = pygame.font.Font('assets/flappybirdnums.ttf', font_size)

        highscore_text = "HighScore"
        scoreref = open("etc/highscore.txt")
        highscore_num = scoreref.read()
        score_text = "Score"
        score_num = str(int(self.score_count))
        
        
        menu_ypos = background_height + ground_height
        border_width = 5
        menu_draw = True
        bird_drawn = False
        bird = None
        
        
        while self.state == "END":
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button1.collidepoint(event.pos):
                        menu_draw = False
                        bird = Bird(self.screen, "assets/blueflappybird.png",background_width/3, background_height/2 )
                        bird_drawn = True
                    elif exit_button1.collidepoint(event.pos):
                        pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if bird:
                        bird.kill()
                        self.state = "GAME"
                if event.type == pygame.QUIT:
                        pygame.quit()
                    
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.rect.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.rect.x = ground2_move.groundMove()

            
            if menu_ypos < background_height/4:
                menu_ypos == background_width/4
            else:
                menu_ypos -= 40
                
            if menu_draw == True:
                
                end_menuscore = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/3) - 10 , menu_ypos, background_width/3, background_height/2))
                border_end_menuscore = pygame.draw.rect(self.screen, "black", (end_menuscore.x - border_width , end_menuscore.y - border_width , end_menuscore.width + (2* border_width), end_menuscore.height + (2* border_width)), border_width)

                play_button1 = pygame.draw.rect(self.screen, (223, 218, 151), (end_menuscore.x -10 , end_menuscore.y + end_menuscore.height + 20 , background_width/6, ground_height))
                border_play_button1 = pygame.draw.rect(self.screen, "black", (play_button1.x - border_width , play_button1.y - border_width , play_button1.width + (2* border_width), play_button1.height + (2* border_width)), border_width)
                
                exit_button1 = pygame.draw.rect(self.screen, (223, 218, 151), (play_button1.x + play_button1.width + 20 , play_button1.y , play_button1.width, play_button1.height))
                border_exit_button1 = pygame.draw.rect(self.screen, "black", (exit_button1.x - border_width , exit_button1.y - border_width , exit_button1.width + (2* border_width), exit_button1.height + (2* border_width)), border_width)
                
                play_triangle_coords = [(play_button1.x + play_button1.width/4, play_button1.y + play_button1.height/6),(play_button1.x + play_button1.width/4, play_button1.y + (2*play_button1.width)/3),(play_button1.x + (4*play_button1.width)/5, play_button1.y + play_button1.height/2)]
                pygame.draw.polygon(self.screen, "green", play_triangle_coords)
                
                x_quit_coords = [(exit_button1.x + exit_button1.width/4, exit_button1.y + exit_button1.height/6),(exit_button1.x + (4*exit_button1.width)/5, exit_button1.y + (2*exit_button1.width)/3), (exit_button1.x + exit_button1.width/4, exit_button1.y + (2*exit_button1.width)/3), (exit_button1.x + (4*exit_button1.width)/5,exit_button1.y + exit_button1.height/6)]
                pygame.draw.line(self.screen, "red", x_quit_coords[0], x_quit_coords[1], 20)
                pygame.draw.line(self.screen, "red", x_quit_coords[2], x_quit_coords[3], 20 )
                
                
                highscore_text_rendered = wordscore_font.render(highscore_text, True, "black")
                highscore_num_rendered = numscore_font.render(highscore_num, True, "black")
                self.screen.blit(highscore_text_rendered, (end_menuscore.x + 20 , end_menuscore.y + end_menuscore.height/6))
                self.screen.blit(highscore_num_rendered, (end_menuscore.x + end_menuscore.width/6 , end_menuscore.y + (2*end_menuscore.height)/5))
                
                score_text_rendered = wordscore_font.render(score_text, True, "black") 
                score_num_rendered = numscore_font.render(score_num, True, "black")
                self.screen.blit(score_text_rendered, (int(end_menuscore.x + ((2* end_menuscore.x)/3)) , end_menuscore.y + end_menuscore.height/6))
                self.screen.blit(score_num_rendered, (end_menuscore.x + (5 * end_menuscore.width)/8 , end_menuscore.y + (2*end_menuscore.height)/5))

               
            if bird_drawn == True:
                bird.drawBird()

            pygame.display.flip()
            clock.tick(60)
