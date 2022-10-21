import pygame as pg, random,time
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3,life





pg.mixer.init()
pg.init()

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
life_6 =  pg.image.load("images/aircraft/6_vidas.png").convert()
life_5 =  pg.image.load("images/aircraft/5_vidas.png").convert()
life_4 =  pg.image.load("images/aircraft/4_vidas.png").convert()
life_3 =  pg.image.load("images/aircraft/3_vidas.png").convert()
life_2 =  pg.image.load("images/aircraft/2_vidas.png").convert()
life_1 =  pg.image.load("images/aircraft/1_vida.png").convert()
nave_imbencible = pg.image.load("images/aircraft/nave.png")
jet = pg.image.load("images/jet.jpg")

pg.display.set_icon(icon)


#sounds
expresions = [
pg.mixer.Sound("Sounds/think.wav"),     
pg.mixer.Sound("Sounds/alive.wav"),
pg.mixer.Sound("Sounds/humble.wav")]

ouch = [
pg.mixer.Sound("Sounds/kick.wav"),     
pg.mixer.Sound("Sounds/shame.wav"),
pg.mixer.Sound("Sounds/point.wav")]

music_stage1 = pg.mixer.Sound("Sounds\Spiegel.wav")
music_stage2 = pg.mixer.Sound("Sounds\Rush.wav")
music_stage2.set_volume(0.1)
music_stage1.set_volume(0.1)

explosion = pg.mixer.Sound("Sounds\explosion.wav")
explosion.set_volume(0.1)
music_stage1.play()


time_clock = pg.time.Clock()
game_over = False

fuente = pg.font.Font(None, 60)
fuente_comunica = pg.font.Font(None, 30)
fuente_stage = pg.font.Font(None, 30)

text_stage1 = "mision: planeta Épsilon"
text_aterriza = "has llegado a la orbita pulsa espacio para aterizar"
mensaje_aterriza = fuente_comunica.render(text_aterriza, 1, (255, 255, 255))
text = "Game Over"

mensaje = fuente.render(text, 1, (255, 255, 255))
mensaje_stage1 = fuente_stage.render(text_stage1, 1,(255,255,255))


swordfish = Aircraft()
asteroide = Asteroid()
swordfish_life = life()

sprite_swordfish = pg.sprite.Group()
sprite_swordfish.add(swordfish)


asteroid=Asteroid() 
asteroid2 = Asteroid2()
asteroid3 = Asteroid3()


asteroids_sprites= pg.sprite.Group()
asteroids_sprites.add(asteroid,asteroid2,asteroid3)

swordfish_life_sprites =pg.sprite.Group()
swordfish_life_sprites.add(swordfish_life)

lifeup = 150
puntuacion= 0

score = 0 
imbencible = 150 
turbo = 0
lifes = 3
final_mision1crono = 0
final_mision2crono = 0
aterrizaje = 0





#######################################################################################################

while not game_over:   
    
    pg.mixer.init()
    pg.init()
    colisiones = pg.sprite.groupcollide(sprite_swordfish,asteroids_sprites,False,False)
    asteroid_score = asteroid.asteroid_score + asteroid2.asteroid_score
    if background_x > -1150.8999999999116:
        tiempo  = pg.time.get_ticks() //1000
        puntuacion = fuente.render("Score: "+str(score+ asteroid_score + aterrizaje ), True,(255, 255, 0))
        screen.blit(puntuacion,(10,10))

    if colisiones and imbencible >= 150 and background_x > -1150.8999999999116:
        swordfish.image = pg.image.load("images/aircraft/explosion.png")
        explosion.play()
        score -= 50
        lifes -= 1 
        ouch[random.randint(0,2)].play()
        imbencible = 0   
    if  imbencible < 150:       
            swordfish.image = pg.image.load("images/aircraft/nave imbencible.png") 
            imbencible += 1
    else:      
      imbencible += 1
      swordfish.image = pg.image.load("images/aircraft/nave.png")
      lifeup  +=1 
       
    vida_up = pg.sprite.groupcollide(sprite_swordfish,swordfish_life_sprites,False,True)

    if vida_up and imbencible >= 150 and background_x > -1150.8999999999116 and lifeup>= 150:
        lifes += 1
        lifeup = 0
        expresions[random.randint(0,2)].play()
    if lifeup < 100:
         swordfish.image = pg.image.load("images/aircraft/nave_lifeup.png")
    if lifeup >= 600:
           swordfish_life_sprites.add(swordfish_life)

    
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y)) 
    asteroid.asteroid_movement()
    asteroid2.asteroid2_movement()
    asteroid3.asteroid3_movement()
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
        #game_over = True
        pass
    ######################buble de aterizaje ##########################################
  
    if background_x <= -1150.8999999999942:
       background_x =  -1150.8999999999942
       screen.blit(mensaje_aterriza,(250,300))
       screen.blit(jet,(700,40))
       if key[pg.K_SPACE]:
          final_mision1crono += 1  
          swordfish.aterrizaje()  
          aterrizaje += 1  
          if final_mision1crono >= 220 :
              music_stage1.set_volume(0.0)  
              music_stage2.play()  
              background_image  = pg.image.load("images\planets\movII.png").convert()
              background_x = 0
              swordfish.rect.center = 100,300             
              asteroid.asteroid_movement2()
              asteroid2.asteroid2_movement2()
              asteroid3.asteroid3_movement2()
              final_mision1crono = 0     
    if aterrizaje == 440:
         game_over = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.6  #0.6 optimo           
    key = pg.key.get_pressed()
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
    pg.time.get_ticks() 
    swordfish_life_sprites.update
    swordfish_life_sprites.draw(screen)
    sprite_swordfish.update()
    sprite_swordfish.draw(screen)
    asteroids_sprites.update()
    asteroids_sprites.draw(screen)
        
    #print(lifes)
    print(aterrizaje)
    
    pg.time.get_ticks()
    pg.display.flip()
     
"""""

 if background_x <= final_mision2:
                 background_x =  final_mision2
                 screen.blit(mensaje_aterriza,(450,300))
                 final_mision1crono += 1
                 swordfish.aterrizaje()
                 """