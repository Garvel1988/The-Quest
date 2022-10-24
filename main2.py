import pygame as pg, random,time
from efects import Sounds,Swordfishchange
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3,life
from screens import Game_screen, Gameover


sound = Sounds() 
swordfishchange = Swordfishchange()
swordfish = Aircraft()
asteroide = Asteroid()
swordfish_life = life()
asteroid=Asteroid() 
asteroid2 = Asteroid2()
asteroid3 = Asteroid3()
gameover =Gameover()
key = pg.key.get_pressed()

#######################################################################################################
def game():
    
    pg.mixer.init()
    pg.init()

    game_over = False



    sound = Sounds() 

    swordfish = Aircraft()
    asteroide = Asteroid()
    swordfish_life = life()
    asteroid=Asteroid() 
    asteroid2 = Asteroid2()
    asteroid3 = Asteroid3()
    gameover =Gameover()
    key = pg.key.get_pressed()
    


    screen = pg.display.set_mode((1000,600))
    pg.display.set_caption("The Quest")

    #images
    background_image  = pg.image.load("images\planets\ilios.png").convert() #1.20 finalizar pantalla
    stage2 = pg.image.load("images\planets\smallpurple.png").convert()
    background_x = 0
    background_y =0
    final_mision1 = -1150.8999999999116
    final_mision2 = -1155.8999999999116
    icon = pg.image.load("images\icon.PNG")
    ###

    life_6 =  pg.image.load("images/aircraft/6_vidas.png").convert()
    life_5 =  pg.image.load("images/aircraft/5_vidas.png").convert()
    life_4 =  pg.image.load("images/aircraft/4_vidas.png").convert()#
    life_3 =  pg.image.load("images/aircraft/3_vidas.png").convert()
    life_2 =  pg.image.load("images/aircraft/2_vidas.png").convert()
    life_1 =  pg.image.load("images/aircraft/1_vida.png").convert()
    nave_imbencible = pg.image.load("images/aircraft/nave.png")
    jet = pg.image.load("images/jet.jpg")

    pg.display.set_icon(icon)

    pg.mixer.init()
    pg.init()

    game_screen =Game_screen() 

    time_clock = pg.time.Clock()

    fuente = pg.font.Font(None, 60)#
    fuente_comunica = pg.font.Font(None, 30) #
    fuente_stage = pg.font.Font(None, 30)

    text_stage1 = "mision: planeta Épsilon"
    text = "Game Over"

    mensaje = fuente.render(text, 1, (255, 255, 255))
    mensaje_stage1 = fuente_stage.render(text_stage1, 1,(255,255,255))

    ##########sprites###############
    
    sprite_swordfish = pg.sprite.Group()
    sprite_swordfish.add(swordfish)

    asteroids_sprites= pg.sprite.Group()
    asteroids_sprites.add(asteroid,asteroid2,asteroid3)

    swordfish_life_sprites =pg.sprite.Group()
    swordfish_life_sprites.add(swordfish_life)

    life_restart = 150 ###
    puntuacion= 0

    score = 0 
    scorelife = 0
    imbencible = 150 
    turbo = 0
    lifes = 3   ###
    final_mision1crono = 0
    final_mision2crono = 0
    landing = 0 ###
    lifeup = 0
    scorelanding = 1
    



    sound.play_music1() 
    while not game_over:      
        pg.init() 
        colisiones = pg.sprite.groupcollide(sprite_swordfish,asteroids_sprites,False,False)         
        asteroid_score = asteroid.asteroid_score + asteroid2.asteroid_score +asteroid3.asteroid_score
        if background_x > -1150.8999999999116: 
            puntuacion = fuente.render("Score: "+str(score+ asteroid_score + landing+ scorelife ), True,(255, 255, 0))
            screen.blit(puntuacion,(10,10))
        if colisiones and imbencible >= 150 and background_x > -1150.8999999999116:
            swordfish.image = pg.image.load("images/aircraft/explosion.png")
            sound.play_explosion()
            score -= 50
            lifes -= 1 
            sound.play_ouch()
            imbencible = 0   
        if imbencible < 150:       
                swordfish.image = pg.image.load("images/aircraft/nave_imbencible.png") 
                imbencible += 1
        else:      
         imbencible += 1
         swordfish.image = pg.image.load("images/aircraft/nave.png")
        
       
        vida_up = pg.sprite.groupcollide(sprite_swordfish,swordfish_life_sprites,False,True)
        if vida_up and imbencible >= 150 and background_x > -1150.8999999999116 and lifeup>= 150:
           lifes += 1
           lifeup = 0
           scorelife += 60
           sound.play_explesion()
        if lifeup >= 600:
           swordfish_life_sprites.add(swordfish_life)

        time_clock.tick(50)
        screen.blit(background_image,(background_x,background_y)) 
        if background_x > -1150.8999999999116:
           asteroid.asteroid_movement()
           asteroid2.asteroid2_movement()
           asteroid3.asteroid3_movement()
        else:
           asteroid.asteroid_noscore()
           asteroid2.asteroid2_noscore()
           asteroid3.asteroid3_noscore()        

        swordfish_life.life_movement()
        sprite_swordfish.update()
        screen.blit(puntuacion,(10,10))
        
        if lifes == 6:
            screen.blit(life_6,(500, 30))
        if lifes == 5:
            screen.blit(life_5,(500, 30))
        if lifes == 4:                                          #funcione de vida
            screen.blit(life_4,(500, 30))
        if lifes == 3:
            screen.blit(life_3,(500, 30))
        if lifes == 2:
            screen.blit(life_2,(500, 30))
        if lifes == 1:
            screen.blit(life_1,(500, 30))
        if lifes == 0:
                sound.switchoffplay1()
                sound.switchoffplay2()
                game_over = True
                
                
            
        
           
    ######################buble de aterizaje ##########################################
     
        if background_x <= -1150.8999999999942:
           background_x =  -1150.8999999999942
           game_screen.landing_radio()
           key = pg.key.get_pressed()
           if key[pg.K_SPACE]:
                final_mision1crono += 1  
                swordfish.aterrizaje()  
                landing += 1
                scorelanding += 1  
                if final_mision1crono >= 220 :
                    sound.switchoffplay1()           
                    sound.play_music2()  
                    background_image  = pg.image.load("images\planets\movII.png").convert()
                    background_x = 0
                    swordfish.rect.center = 100,300             
                    asteroid.asteroid_movement2()
                    asteroid2.asteroid2_movement2()
                    asteroid3.asteroid3_movement2()
                    final_mision1crono = 0     
    
                        ###################################################################33
        for event in pg.event.get():
            if event.type == pg.QUIT or key[pg.K_ESCAPE]:
               game_over = True
               sound.switchoffplay1
               sound.switchoffplay2
        key = pg.key.get_pressed()  
        background_x -= 3.6  #0.6 optimo           
        if not key[pg.K_UP]and not key[pg.K_DOWN]:
            turbo = 0
            swordfish.vy = 4
        if key[pg.K_UP]:
            turbo +=20
            swordfish.go_up()
            if turbo >= 500:
                swordfish.vy = 10
                swordfish.image = pg.image.load("images/aircraft/naveup_turbo.png")
            if  imbencible < 150:
                swordfish.image = pg.image.load("images/aircraft/nave_imbencibleup.png")         
        if key[pg.K_DOWN]:
            turbo +=20
            swordfish.go_down()
            if turbo >= 500:
                swordfish.vy = 10
                swordfish.image = pg.image.load("images/aircraft/navedown_turbo.png")
            if  imbencible < 150:
                swordfish.image = pg.image.load("images/aircraft/nave_imbencibledown.png")   
        swordfish_life_sprites.update
        swordfish_life_sprites.draw(screen)
        sprite_swordfish.update()
        sprite_swordfish.draw(screen)
        asteroids_sprites.update()
        asteroids_sprites.draw(screen)
        total_score = score+ asteroid_score + landing+ scorelife     
        if landing == 440:
            sound.switchoffplay1()
            sound.switchoffplay2()
            game_over = True

        pg.time.get_ticks()
        pg.display.flip()
        
    

    return total_score
    
    

