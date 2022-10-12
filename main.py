import pygame as pg
from objects import aircraft

pg.mixer.init()
pg.init()
screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")
backgorund_image  = pg.image.load("images\stratosphere1.JPG").convert()
icon = pg.image.load("images\icon.PNG")
pg.display.set_icon(icon)

sonido_fondo = pg.mixer.Sound("Sounds\Rush.wav")
time_clock = pg.time.Clock()
nave = aircraft(20,300, w=30, h=50,color=(229,190,1))
nave.vy = 5
game_over = False
x = 0
y =-240

#nave = pg.image.load("starcraft.PNG")#
sonido_fondo.play()
while not game_over:
   # pg.mixer.Sound.play(sonido_fondo)
    dt = time_clock.tick(50)
    screen.blit(backgorund_image,(x,y,))
    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    x -= 0.3
    nave.movement(pg.K_UP, pg.K_DOWN)
    nave.loader(screen)
    
    pg.display.flip()
