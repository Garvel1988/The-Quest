
import pygame
import sys
from efects import *
from objects import *
from score import *

sound = Sounds()



class Game_screen():
    def __init__(self):
       self.screen = pygame.display.set_mode((1000,600))
       self.background_image  = pygame.image.load("images\planets\ilios.png").convert() #1.20 finalizar pantalla
       self.stage2 = pygame.image.load("images\planets\smallpurple.png").convert()
       self.background_x = 0
       self.background_y =0
       self.final_mision1 = -1150.8999999999116
       self.final_mision2 = -1155.8999999999116
       self.icon = pygame.image.load("images\icon.PNG")
       self.fuente_comunica = pygame.font.Font(None, 30)
       self.text_aterriza = "has llegado a la orbita manten DCHA para piloto automatico"
       self.mensaje_aterriza = self.fuente_comunica.render(self.text_aterriza, 1, (255, 255, 255))
       self.jet = pygame.image.load("images/jet.jpg")



    def landing_radio(self):
          self.screen.blit(self.mensaje_aterriza,(250,300))
          self.screen.blit(self.jet,(700,40))



########################################################################################################


class Intro():
   def __init__(self):
     pygame.init()
     self.playing = False
     self.screen_intro = pygame.display.set_mode((1000,600))
     self.background_image  = pygame.image.load("images\space.jpg").convert()
     self.background_image_x =0
     self.background_image_y = -400
     self.image_nave = pygame.image.load("images/navetitulo.png").convert()
     self.font = pygame.font.Font(None, 30)
     self.continue_text = "press SPACE to continue"
     self.tocontinue = self.font.render(self.continue_text, 1, (255, 255, 255))
     self.music_opening = pygame.mixer.Sound("Sounds\opening.wav")
     self.music_opening.set_volume(0.1)
     self.key = pygame.key.get_pressed()
     self.counter = 0
     self.inst = 0
    

   def intro_screen1(self):
    self.music_opening.play()
    while not self.playing:
        pygame.init()
        pygame.display.set_caption("The Quest")
        #print(self.counter)
        self.key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.key[pygame.K_SPACE]:
               self.playing = True
               self.music_opening.set_volume(0.0)
        self.background_image_y += 0.1
        if self.background_image_y >= 5:
           self.background_image_y = 5
           self.background_image  = pygame.image.load("images\spacequest.jpg").convert() 
           self.counter += 1 
           if self.counter >= 320:     
              self.background_image  = pygame.image.load("images\instrucciones.jpg").convert()
              if self.counter >= 483: 
                 self.background_image  = pygame.image.load("images\instrucciones2.jpg").convert()
                 if self.counter >= 640:
                    self.background_image  = pygame.image.load("images\instrucciones3.jpg").convert()
                    if self.counter >=790:
                       self.counter = 0               
        self.screen_intro.blit(self.background_image,(self.background_image_x,self.background_image_y))
        self.screen_intro.blit(self.tocontinue,(350,500))
        pygame.display.update()
    #pygame.quit()
    
    
##################################################################################################


class Gameover():
   def __init__(self):
       super().__init__()
       pygame.init()
       self.screen_over = pygame.display.set_mode((1000,600))
       self.background  = pygame.image.load("images\endgame.jpg").convert()
       self.background_x =0
       self.background_y = 0
       self.font = pygame.font.Font(None, 30)
       self.continue_text = "press SPACE to continue"
       self.tocontinue = self.font.render(self.continue_text, 1, (255, 255, 255))
       self.gameover = pygame.mixer.Sound("Sounds\gameover.wav")
       self.gameover.set_volume(0.1)
       self.key = pygame.key.get_pressed()
       self.playing = False

   def gameover_screen(self):
        while not self.playing:
            pygame.init()
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT or key[pygame.K_SPACE]:
                    self.playing = True
            self.screen_over.blit(self.background,(0,0))
            self.screen_over.blit(self.tocontinue,(350,500))
            pygame.display.flip()
        pygame.quit()




   ################################################################


class Congratulations():
     def __init__(self):
       pygame.init()
       self.screen_congrat = pygame.display.set_mode((1000,600))
       self.backgroundcongrat  = pygame.image.load("images\congratulations.jpg").convert()
       self.backgroundcongrat_x =0
       self.backgroundcongrat_y = 0
       self.font = pygame.font.Font(None, 30)
       self.continue_text = "MISSION  ACCOMPLISHED"
       self.tocontinue = self.font.render(self.continue_text,1, (255, 255, 255))
       self.key = pygame.key.get_pressed()
       self.playing = False

       self.backgroundcredits  = pygame.image.load("images/nigth_sky.jpg").convert()
       self.counter = 0
       self.credits_text1 = " CREDITS"
       
       self.screen_credtis = pygame.display.set_mode((1000,600))
       self.text_box = pygame.Rect(10,10,40,120)
       self.x = 350
       self.y = 100

     def congratulations_screen(self):
        pygame.init()
        sound.congratulation()
        while not self.playing:
    
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT or key[pygame.K_SPACE]:
                    self.playing = True
                    sound.switchoffcongratulation()
            self.screen_congrat.blit(self.backgroundcongrat,(0,0))
            self.screen_congrat.blit(self.tocontinue,(350,500))
            pygame.display.flip()
    
        
    



     def credits_screen(self):
            pygame.init()
            sound.credits()
            while not self.playing:
                self.counter += 1
                for event in pygame.event.get():
                    key = pygame.key.get_pressed()
                    if event.type == pygame.QUIT or key[pygame.K_SPACE]:
                        self.playing = True          
                if self.counter == 2000:
                   self.credits_text1 = "Producer   Ruben.Velasco"
                if self.counter == 4000:
                    self.credits_text1 = "Designer  Ruben.Velasco"
                if self.counter == 6000:
                    self.credits_text1 = "Audio Cowboy bebop soundtrack"
                if self.counter == 8000:
                    self.credits_text1 = "2D artist Ruben.Velasco"
                if self.counter == 10000:
                    self.credits_text1 = "Contact Robingarvel@gmail.com"
                if self.counter == 12000:
                   self.credits_text1 = "Thanks to Keepcoding Academy"
                if self.counter > 14000:
                          self.counter = 0
                self.screen_credtis.blit(self.backgroundcredits,(-70,-200))
                self.credit_render = self.font.render(self.credits_text1,1, (255, 255, 255))
                self.screen_credtis.blit(self.credit_render,(self.x,self.y))               
                pygame.display.flip() 

"""
screen_congrat = pygame.display.set_mode((1000,600))
    backgroundcongrat_x =0
    backgroundcongrat_y = 0
    font = pygame.font.Font(None, 30)
    continue_text = "MISSION  ACCOMPLISHED"
    tocontinue = font.render(continue_text,1, (255, 255, 255))
    key = pygame.key.get_pressed()
    credit = True
    backgroundcredits  = pygame.image.load("images/nigth_sky.jpg").convert()
    counter = 0
    credits_text1 = " CREDITS" 
    screen_credtis = pygame.display.set_mode((1000,600))
    text_box = pygame.Rect(10,10,40,120)
    x = 350
    y = 100


    while credit:
        sound.credits()
        counter += 1
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT or key[pygame.K_c]:
               credit = False
            if key[pg.K_x]:
               exit()                       
        if counter == 2000:
            credits_text1 = "Producer   Ruben.Velasco"
        if counter == 4000:
            credits_text1 = "Designer  Ruben.Velasco"
        if counter == 6000:
            credits_text1 = "Audio Cowboy bebop soundtrack"
        if counter == 8000:
            credits_text1 = "2D artist Ruben.Velasco"
        if  counter == 10000:
            credits_text1 = "Contact Robingarvel@gmail.com"
        if counter == 12000:
            credits_text1 = "Thanks to Keepcoding Academy"
        if counter > 14000:
            counter = 0
        screen_credtis.blit(backgroundcredits,(-70,-200))
        credit_render = font.render(credits_text1,1, (255, 255, 255))
        screen_credtis.blit(credit_render,(x,y))               
        pygame.display.flip()      
    pg.quit































class Scorecredits():
     def __init__(self):
        pygame.init()
        self.player1 = read_Rows("Score")
        self.player2 = read_Rows2("Score")
        self.player3 = read_Rows3("Score")
        self.player4 = read_Rows4("Score")
        self. player5 = read_Rows5("Score")    
        self.screen_over = pg.display.set_mode((1000,600))
        self.background  = pg.image.load("images\exosphere.jpg").convert()
        self.background_x =0
        self.background_y = 0
        self.font = pg.font.Font(None, 60)
        self.textplayer1= (self.player1)
        self.textplayer2 =(self.player2)
        self.textplayer3= (self.player3)
        self.extplayer4 =(self.player4)
        self.textplayer5= (self.player5)
        self.playerrender = self.font.render(self.player1, 1, (255, 255, 0))
        self.playe2render = self.font.render(self.player2, 1, (255, 255, 0))
        self.playe3render = self.font.render(self.player3, 1, (255, 255, 0))
        self.playe4render = self.font.render(self.player4, 1, (255, 255, 0))
        self.playe5render = self.font.render(self.player5, 1, (255, 255, 0))


        self.credits_music = pg.mixer.Sound("Sounds\gameover.wav")
        self.credits_music.set_volume(0.1)
        self.key = pg.key.get_pressed() 
        self.playing = False

     def scorecredtis_screen(self):
        while not self.playing:
            self.credits_music.play
            pg.init()
            for event in pg.event.get():
                self.key = pg.key.get_pressed()
                if event.type == pg.QUIT or self.key[pg.K_ESCAPE]:
                    self.playing = True
        self.screen_over.blit(self.background,(0,0))
        self.screen_over.blit(self.playerrender,(370,50))
        self.screen_over.blit(self.playe2render,(370,140))
        self.screen_over.blit(self.playe4render,(370,320))
        self.screen_over.blit(self.playe5render,(370,410))
        pg.display.flip()
    
     pygame.quit()

"""


