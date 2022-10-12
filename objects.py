import pygame as pg


class aircraft:
   def __init__(self,center_x, center_y, w =30, h=35,color=(255,255,0)):
     self.center_x =center_x
     self.center_y = center_y
     self.color = color
     self.w = w
     self.h = h
     self.vx = 0
     self.vy = 0

   def movement(self, tecla_arriba, tecla_abajo, y_max=600):
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[tecla_arriba] and self.center_y > 0 + self.h//2:
            self.center_y -= self.vy
        if estado_teclas[tecla_abajo]:
            self.center_y += self.vy
        if self.center_y > y_max - self.h//2:
           self.center_y = y_max - self.h //2
    
   def loader(self, pantalla):
        pg.draw.rect(pantalla,self.color,(self.center_x -self.w//2 ,self.center_y -self.h //2 ,self.w, self.h))

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