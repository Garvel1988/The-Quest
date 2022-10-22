
import pygame, random
background_x = 0
final_mision1 = -1150.8999999999116


class Aircraft(pygame.sprite.Sprite):
    def __init__(self):
        super(Aircraft, self).__init__()
        self.image = pygame.image.load("images/aircraft/nave.png")
        self.rect = self.image.get_rect()
        self.rect.center = 100,300
        self.vy = 4
        self.lifes = 3
        self.life_restart = 150
        self.landing = 0
        self.life_3 =  pygame.image.load("images/aircraft/3_vidas.png")



           
    def go_up(self):
        self.rect.y -= self.vy
        self.image = pygame.image.load("images/aircraft/naveup.png")

        if self.rect.centery < 40:
           self.rect.y += self.vy

    def go_down(self):
        self.rect.y += self.vy
        self.image = pygame.image.load("images/aircraft/navedown.png")

        if self.rect.y > 530:
           self.rect.y -= self.vy

    def aterrizaje(self):
           self.rect.x += self.vy        
           if self.rect.x >= 675:
              self.image = pygame.transform.scale(self.image, (50, 40))
              if self.rect.x >= 700:
                self.rect.y -= self.vy
                self.image = pygame.transform.rotate(self.image, 75)
                self.image = pygame.transform.scale(self.image, (20, 30))
                
    
              

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroids/asteroid2.png")
        self.rect = self.image.get_rect()
        #self._spritex = random.randint(2,15)
        self.rect.center = 4000,random.randint(100,600)
        self.speed = random.randint(10,15) #velocidad
        self.asteroid_score = 0

        
    def asteroid_movement(self):
        self.rect.x -= self.speed
        #self.rect.centerx = self._spritex
   
        if self.rect.left < -30 and background_x > -1150.8999999999116:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 10

    def asteroid_movement2(self):
        self.rect.center = 4000,random.randint(100,600)
        self.speed = random.randint(15,18)
        self.rect.x -= self.speed
        #self.rect.centerx = self._spritex
   
        if self.rect.left < -30:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 10
            
                       
        
class Asteroid2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroids/asteroid1.png")
        self.rect = self.image.get_rect()
        self.rect.center = 4000,random.randint(100,600)
        self.speed = random.randint(8,15)
        self.asteroid_score = 0
        
    
    def asteroid2_movement(self,):
        self.rect.x -= self.speed
        

        if self.rect.left < -100 and background_x > -1150.8999999999116:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 20
   
    def asteroid2_movement2(self,):
        self.rect.center = 4000,random.randint(100,600)
        self.speed = random.randint(10,16)
        self.rect.x -= self.speed
        

        if self.rect.left < -100 and background_x > -1150.8999999999116:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 20        
            
            
            

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroids/asteroid3.png")
        self.rect = self.image.get_rect()
        self.rect.center = 3000,random.randint(100,600)
        self.speed = random.randint(2,4)
        self.asteroid_score = 0
        
    def asteroid3_movement(self):
        self.rect.x -= self.speed

        if self.rect.left < -300 and background_x > -1150.8999999999116:
            self._spritex=3100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 40
        
    def asteroid3_movement2(self):
        self.rect.center = 3000,random.randint(100,600)
        self.speed = random.randint(4,8)
        self.rect.x -= self.speed

        if self.rect.left < -300 and background_x > -1150.8999999999116:
            self._spritex=3100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            self.asteroid_score += 40


class life(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/aircraft/swordfish_life.png")
        self.rect = self.image.get_rect()
        self.rect.center = 8000,random.randint(100,600)
        self.speed = random.randint(12,20)
        self.life_score = 0
    
        
    
    def life_movement(self):
        self.rect.x -= self.speed

        if self.rect.left < -300:
            self._spritex=3100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 8000,random.randint(100,600)





class Intro():
   def __init__(self):
     self.intro_screen = False
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
    while not self.intro_screen:
        pygame.init()
        print(self.counter)
        self.key = pygame.key.get_pressed()
        self.music_opening.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.key[pygame.K_SPACE]:
               self.intro_screen = True
        self.background_image_y += 0.1
        if self.background_image_y >= 5:
           self.background_image_y = 5
           self.background_image  = pygame.image.load("images\spacequest.jpg").convert() 
           self.counter += 1 
           if self.counter >= 320:     
              self.background_image  = pygame.image.load("images\instrucciones.jpg").convert()
              if self.counter >= 483: 
                 self.background_image  = pygame.image.load("images\instrucciones2.jpg").convert()
                 if self.counter >= 590:
                    self.background_image  = pygame.image.load("images\instrucciones3.jpg").convert()
                    if self.counter >=700:
                       self.counter = 0               
        self.screen_intro.blit(self.background_image,(self.background_image_x,self.background_image_y))
        self.screen_intro.blit(self.tocontinue,(350,500))
        #self.screen_intro.blit(self.image_nave,(self.background_image_x,self.background_image_y))
        pygame.display.update()
    pygame.quit()
    


