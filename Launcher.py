from cgitb import text
import pygame as pg
from efects import Sounds
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3,life
from screens import Game_screen, Gameover, Intro
from main2 import game
from score import *


gameover = Gameover()
sound = Sounds() 
pg.mixer.init()
pg.init()
#########################################################3


intro = Intro()
intro.intro_screen1()

score = game()
print(score)


pg.init()    
screen_over = pg.display.set_mode((1000,600))
background  = pg.image.load("images\endgame.jpg").convert()
background_x =0
background_y = 0
font = pg.font.Font(None, 30)
continue_text = "press SPACE to continue"
tocontinue = font.render(continue_text, 1, (255, 255, 255))
gameover = pg.mixer.Sound("Sounds\gameover.wav")
gameover.set_volume(0.1)
key = pg.key.get_pressed()
playing = False

score_text = "SCORE  " + str(score)
fontscore  =  pg.font.Font(None, 60)
scorepint = fontscore.render(score_text,1,(255,255,0))

name_font = pg.font.Font(None, 60)
text_name = ""



while not playing:
        pg.init()
        gameover.play()
        screen_over 
        background
        for event in pg.event.get():
            key = pg.key.get_pressed()
            if event.type == pg.QUIT or key[pg.K_SPACE]:
                playing = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    text_name = text_name[:-1]
                else:
                    text_name += event.unicode
                if len(text_name) >3:
                    text_name = text_name[:-1]           
        text_surface = name_font.render(text_name,1,(255,255,0))
        screen_over.blit(background,(0,0))
        screen_over.blit(tocontinue,(350,500))
        screen_over.blit(scorepint,(350,50))
        screen_over.blit(text_surface,(330,200))
        pg.display.update()
pg.quit()

text_name = text_name.upper()
print(text_name)

if __name__ == "__main__":
    #createDB()
    #createTable()
    #inser_row(text_name, score)
    read_ordered("Score")




pg.init()    
screen_over = pg.display.set_mode((1000,600))
background  = pg.image.load("images\endgame.jpg").convert()
background_x =0
background_y = 0
font = pg.font.Font(None, 30)
continue_text = "Credits" + str(read_ordered("Score"))
tocontinue = font.render(continue_text, 1, (255, 255, 255))
gameover = pg.mixer.Sound("Sounds\gameover.wav")
gameover.set_volume(0.1)
key = pg.key.get_pressed()
playing = False



while not playing:
    pg.init()
    for event in pg.event.get():
       key = pg.key.get_pressed()
       if event.type == pg.QUIT or key[pg.K_SPACE]:
          playing = True
    screen_over.blit(background,(0,0))
    screen_over.blit(tocontinue,(350,500))
    pg.display.flip()
  
pg.quit()

