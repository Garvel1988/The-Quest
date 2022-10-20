from string import punctuation
import pygame, random, time

background_x = 0
final_mision1 = -1150.8999999999116

class Aircraft(pygame.sprite.Sprite):
    def __init__(self):
        super(Aircraft, self).__init__()
        self.image = pygame.image.load("images/aircraft/nave.png")
        self.rect = self.image.get_rect()
        self.rect.center = 100,300
        self.vy = 4
           

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
           
              
              
           
            
        



class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroids/asteroid2.png")
        self.rect = self.image.get_rect()
        #self._spritex = random.randint(2,15)
        self.rect.center = 4000,random.randint(100,600)
        self.speed = random.randint(15,20) #velocidad
        self.asteroid_score = 0

        
    def asteroid_movement(self):
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
        

        if self.rect.left < -100:
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

        if self.rect.left < -300:
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
        self.asteroid_score = 0
    
        
    
    def life_movement(self):
        self.rect.x -= self.speed

        if self.rect.left < -300:
            self._spritex=3100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 8000,random.randint(100,600)
            self.asteroid_score += 60
 


""""
Turn_up = [pygame.image.load("aircraft\image1.PNG"),
           pygame.image.load("aircraft\image2.PNG"),
           pygame.image.load("aircraft\image3.PNG"),
           pg.image.load("aircraft\image4.PNG"),
           pg.image.load("aircraft\image5.PNG"),
           pg.image.load("aircraft\image6.PNG"),
] 

turn_Down=[pg.image.load("aircraft\imageabajo1.PNG"),
           pg.image.load("aircraft\imageabajo2.PNG"),
           pg.image.load("aircraft\imageabajo3.PNG"),
           pg.image.load("aircraft\imageabajo4.PNG"),
           pg.image.load("aircraft\imageabajo5.PNG"),
           pg.image.load("aircraft\imageabajo6.PNG"),
]
"""
""""
   def loader():
    imagen = pg.image.load("starcraft.PNG")
    pg.transform.scale(imagen, [30, 30])
   
  """   