import pygame as pg, random,time
from efects import Sounds
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3,life
from screens import Game_screen, Gameover, Intro
from main2 import game


gameover = Gameover()
sound = Sounds() 
pg.mixer.init()
pg.init()
#########################################################3


intro = Intro()
intro.intro_screen1()

juego = game()
print(juego)


pg.init()    
screen_over = pg.display.set_mode((1000,600))
background  = pg.image.load("images\gameover.jpg").convert()
background_x =0
background_y = 0
font = pg.font.Font(None, 30)
continue_text = "press SPACE to continue"+ str(juego)
tocontinue = font.render(continue_text, 1, (255, 255, 255))
gameover = pg.mixer.Sound("Sounds\gameover.wav")
gameover.set_volume(0.1)
key = pg.key.get_pressed()
playing = False

score_text = "SCORE  " + str(juego)
fontscore  =  pg.font.Font(None, 60)
scorepint = fontscore.render(score_text,1,(255,255,0))

while not playing:
        pg.init()
        gameover.play()
        screen_over 
        background
        for event in pg.event.get():
            key = pg.key.get_pressed()
            if event.type == pg.QUIT or key[pg.K_SPACE]:
                playing = True
            screen_over.blit(background,(0,0))
            screen_over.blit(tocontinue,(350,500))
            screen_over.blit(scorepint,(350,50))
        pg.display.update()
pg.quit()







