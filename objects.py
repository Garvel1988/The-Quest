import pygame, random


class Aircraft(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Aircraft, self).__init__()
        self.image = pygame.image.load("images/aircraft/nave.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self._vy = 5  # The x-velocity.
       # self._spritex = pos[0]
        self._spritey = position[1]

    def go_up(self):
        # Update the _spritex position first and then the rect.
        self._spritey -= self._vy
        self.rect.centery = self._spritey

        if self.rect.centery < 40:
           self._spritey += self._vy


    def go_down(self):
        self._spritey += self._vy
        self.rect.centery = self._spritey

        if self.rect.centery > 550:
           self._spritey -= self._vy

        


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroids/asteroid2.png")
        self.rect = self.image.get_rect()
        #self._spritex = random.randint(2,15)
        self.rect.center = 1000,random.randint(100,600)
        self.speed = random.randint(15,20) #velocidad

        
    def asteroid_movement(self):
        self.rect.x -= self.speed
        #self.rect.centerx = self._spritex

        if self.rect.left < -30:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
            
class Asteroid2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroids/asteroid1.png")
        self.rect = self.image.get_rect()
        self.rect.center = 1000,random.randint(100,600)
        self.speed = random.randint(8,15)
        
    def update2(self):
        self.rect.x -= self.speed

        if self.rect.left < -100:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroids/asteroid3.png")
        self.rect = self.image.get_rect()
        self.rect.center = 1000,random.randint(100,600)
        self.speed = random.randint(8,15)
        
    def update2(self):
        self.rect.x -= self.speed

        if self.rect.left < -100:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)    

""""

static_aircraft = [pg.image.load("aircraft\image.PNG")]

Turn_up = [pg.image.load("aircraft\image1.PNG"),
           pg.image.load("aircraft\image2.PNG"),
           pg.image.load("aircraft\image3.PNG"),
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