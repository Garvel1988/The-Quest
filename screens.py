
from calendar import c
import pygame
import sys

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
       self.text_aterriza = "has llegado a la orbita pulsa espacio para aterizar"
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

       

       #self.puntuacion = self.font.render("Score: "+str(total_score2), True,(255, 255, 0))

   def gameover_screen(self):
        while not self.playing:
            pygame.init()
            self.gameover.play()
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT or key[pygame.K_SPACE]:
                     sys.exit()
            self.screen_over.blit(self.background,(0,0))
            self.screen_over.blit(self.tocontinue,(350,500))
            pygame.display.flip()
        pygame.quit()




   ################################################################

""""
        self.screen_over = pygame.display.set_mode((1000,600))
        self.background  = pygame.image.load("images\endgame.jpg").convert()
        background_x =0
        background_y = 0
        font = pygame.font.Font(None, 30)
        continue_text = "press SPACE to continue"
        tocontinue = font.render(continue_text, 1, (255, 255, 255))
        gameover = pygame.mixer.Sound("Sounds\gameover.wav")
        gameover.set_volume(0.1)
        key = pygame.key.get_pressed()
        playing = False

        score_text = "SCORE  " + str(juego)
        fontscore  =  pygame.font.Font(None, 60)
        scorepint = fontscore.render(score_text,1,(255,255,0))

        while not playing:
                pygame.init()
                gameover.play()
                screen_over 
                background
                for event in pygame.event.get():
                    key = pygame.key.get_pressed()
                    if event.type == pg.QUIT or key[pg.K_SPACE]:
                        playing = True
                    screen_over.blit(background,(0,0))
                    screen_over.blit(tocontinue,(350,500))
                    screen_over.blit(scorepint,(350,50))
                pygame.display.update()
        pygame.quit()

 
 



class Congratulations():
     def __init__(self):
       pygame.init()
       self.screen_congrat = pygame.display.set_mode((1000,600))
       self.backgroundcongrat  = pygame.image.load("images\congratulations.jpg").convert()
       self.backgroundcongrat_x =0
       self.backgroundcongrat_y = 0
       self.font = pygame.font.Font(None, 30)
       self.continue_text = "Congratulations"
       self.tocontinue = self.font.render(self.continue_text, 1, (255, 255, 255))
       self.gameover = pygame.mixer.Sound("Sounds\gameover.wav")
       self.gameover.set_volume(0.1)
       self.key = pygame.key.get_pressed()
       self.playing = False
    
     def congratulations_screen(self):
        while not self.playing:
            self.gameover.play()
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT or key[pygame.K_SPACE]:
                    self.playing = True
            pygame.display.flip()
"""