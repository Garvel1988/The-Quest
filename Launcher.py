from asyncore import read
from cgitb import text
from dataclasses import field
from functools import total_ordering
import pygame as pg
from efects import Sounds
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3,life
from screens import*
from main2 import game
from score import *


gameover = Gameover()
sound = Sounds() 
pg.mixer.init()
pg.init()
running = False
screens = Congratulations()
read_ordered("score")
player_comparison = read_Rows6("Score")  
#########################################################3
while not running:
    pg.init()
    key = pg.key.get_pressed() 
    intro = Intro()
    intro.intro_screen1()   ########## intro del juego######
    totalgamescore = game() ##########juego ##########
    pg.quit()
    ###############pantalla de escribir iniciales################
    if totalgamescore > int(player_comparison):
        pg.init()    
        screen_over = pg.display.set_mode((1000,600))
        background  = pg.image.load("images\endgame.jpg").convert()
        background_x =0
        background_y = 0
        font = pg.font.Font(None, 30)
        write_text = "Write your initials and press SPACE to continue"
        write_tocontinue = font.render(write_text, 1, (255, 255, 255))
        gameover = pg.mixer.Sound("Sounds\gameover.wav")
        gameover.set_volume(0.1)
        key = pg.key.get_pressed()
        playing = False
        score_text = "SCORE  " + str(totalgamescore)
        fontscore  =  pg.font.Font(None, 60)
        scorepint = fontscore.render(score_text,1,(255,255,0))
        name_font = pg.font.Font(None, 160)
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
                        
                text_surface = name_font.render(text_name.upper(),1,(255,255,0))
                screen_over.blit(background,(0,0))
                screen_over.blit(write_tocontinue,(270,500))
                screen_over.blit(scorepint,(350,50))
                screen_over.blit(text_surface,(330,200))
                pg.display.update()
        pg.quit()
        text_name = text_name.upper()
        print(text_name)
        if __name__ == "__main__":
            #¡#createDB()                          ####funciones de SQLITE########
            #createTable()
            #read_ordered("score")     
            inser_row(text_name,totalgamescore )


    if totalgamescore<= int(player_comparison):
        pg.init() 
        screen_over = pg.display.set_mode((1000,600))
        backgroundover  = pg.image.load("images\gameover.jpg").convert()
        background_x =0
        background_y = 0
        font = pg.font.Font(None, 30)
        write_textover = "press SPACE to continue"
        write_tocontinue = font.render(write_textover, 1, (255, 255, 255))
        gameover = pg.mixer.Sound("Sounds\gameover.wav")
        gameover.set_volume(0.1)
        key = pg.key.get_pressed()
        playing = False
        score_text = "SCORE  " + str(totalgamescore)
        fontscore  =  pg.font.Font(None, 60)
        scorepint = fontscore.render(score_text,1,(255,255,0))
        name_font = pg.font.Font(None, 160)
        text_name = ""
        while not playing:
                pg.init()
                gameover.play()
                screen_over 
                backgroundover
                for event in pg.event.get():
                    key = pg.key.get_pressed()
                    if event.type == pg.QUIT or key[pg.K_SPACE]:
                        playing = True
                screen_over.blit(backgroundover,(0,0))
                screen_over.blit(write_tocontinue,(320,500))
                screen_over.blit(scorepint,(350,50))
                pg.display.update()
        pg.quit()


    read_ordered("score")

    player1 = read_Rows("Score")
    player2 = read_Rows2("Score")
    player3 = read_Rows3("Score")
    player4 = read_Rows4("Score")
    player5 = read_Rows5("Score")     
    pg.init()    
    screen_over = pg.display.set_mode((1000,600))
    background  = pg.image.load("images\exosphere.jpg").convert()
    background_x =0
    background_y = 0
    font = pg.font.Font(None, 60)
    font_continue =pg.font.Font(None,30)
    textplayer1= (player1)
    textplayer2 =(player2)
    textplayer3= (player3)
    textplayer4 =(player4)
    textplayer5= (player5)
    continue_text = "press SPACE to continue or X to Windows"

    tocontinuegame = font_continue.render(continue_text, 1, (255, 255, 255))
    playerrender = font.render(player1, 1, (255, 255, 0))
    playe2render = font.render(player2, 1, (255, 255, 0))
    playe3render = font.render(player3, 1, (255, 255, 0))
    playe4render = font.render(player4, 1, (255, 255, 0))
    playe5render = font.render(player5, 1, (255, 255, 0))
    credits_music = pg.mixer.Sound("Sounds\gameover.wav")
    #gameover.set_volume(0.1)
    key = pg.key.get_pressed() 
    scores = False
                                                  ############pantalla de Records##################
    while not scores:
        sound.scores()
        pg.init()
        for event in pg.event.get():
             key = pg.key.get_pressed()
             if event.type == pg.QUIT or key[pg.K_SPACE]:
                scores = True 
             if key[pg.K_x]:
               exit() 
        screen_over.blit(background,(0,0))
        screen_over.blit(playerrender,(370,50))
        screen_over.blit(playe2render,(370,140))
        screen_over.blit(playe3render,(370,230))
        screen_over.blit(playe4render,(370,320))
        screen_over.blit(playe5render,(370,410))
        screen_over.blit(tocontinuegame,(280,500)) 
        pg.display.flip()
        pg.display.update()
    pg.quit()   
                                                          #####pantala de fin de juego######

    pg.init()
    screen_congrat = pygame.display.set_mode((1000,600))
    backgroundcongrat_x =0
    backgroundcongrat_y = 0
    font = pygame.font.Font(None, 30)
    misioxn_text = "MISSION  ACCOMPLISHED"
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
    continue_text = "press SPACE to continue or X to Windows"




    while credit:
        sound.credits()
        counter += 1
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT or key[pygame.K_SPACE]:
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
        screen_congrat.blit(tocontinuegame,(250,550))             
        pygame.display.flip()      
    pg.quit()