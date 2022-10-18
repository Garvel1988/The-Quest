from time import sleep
import pygame as pg, random
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3


pg.mixer.init()
pg.init()



screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")

#images
background_image  = pg.image.load("images\planets\small.png").convert() #1.20 finalizar pantalla
background_x = 0
background_y =0
final_mision1 = -1185.8999999999116
icon = pg.image.load("images\icon.PNG")
life_3 =  pg.image.load("images/aircraft/3vidas.png").convert()
life_2 =  pg.image.load("images/aircraft/2vidas.png").convert()
life_1 =  pg.image.load("images/aircraft/1vida.png").convert()
nave_imbencible = pg.image.load("images/aircraft/nave.png")

pg.display.set_icon(icon)

""""
def colisiones():
    pg.sprite.groupcollide(sprite_swordfish,asteroids_sprites,True,False)
    pg.time.delay(1000)
"""

#sounds
music = pg.mixer.Sound("Sounds\Rush.wav")
music.set_volume(0.1)
explosion = pg.mixer.Sound("Sounds\explosion.wav")
explosion.set_volume(0.1)
music.play()


time_clock = pg.time.Clock()
game_over = False

fuente = pg.font.Font(None, 60)
fuente_comunica = pg.font.Font(None, 30)

text_aterriza = "has llegado a la orbita pulsa espacio para aterizar"
mensaje_aterriza = fuente_comunica.render(text_aterriza, 1, (255, 255, 255))
text = "Game Over"

mensaje = fuente.render(text, 1, (255, 255, 255))

swordfishx = 100
swordfishy = 300
swordfish = Aircraft()
asteroide = Asteroid()


sprite_swordfish = pg.sprite.Group()
sprite_swordfish.add(swordfish)

asteroid=Asteroid() 
asteroid2 = Asteroid2()
asteroid3 = Asteroid3()
asteroids_sprites= pg.sprite.Group()
asteroids_sprites.add(asteroid,asteroid2,asteroid3)


background_time = 0
lifes = 3
score = 0 
imbencible = 150 



while not game_over:
    asteroid_score = asteroid.asteroid_score + asteroid2.asteroid_score
    tiempo  = pg.time.get_ticks() //1000
    puntuacion = fuente.render("Score: "+str(tiempo + score+ asteroid_score ), True,(255, 255, 0))
    screen.blit(puntuacion,(10,10))
    
    #iniciadores
    
    #colisiones
    colisiones = pg.sprite.groupcollide(sprite_swordfish,asteroids_sprites,False,False)
    
    if colisiones and imbencible >= 150 and background_x >= -1150.8999999999116:
        swordfish.image = pg.image.load("images/aircraft/explosion.png")
        explosion.play()
        score -= 50
        lifes -= 1 
        imbencible = 0   
    if  imbencible < 150:
            swordfish.image = pg.image.load("images/aircraft/nave imbencible.png") 
            imbencible += 1
    else:      
      imbencible += 1
      swordfish.image = pg.image.load("images/aircraft/nave.png") 
      
    
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y)) 
    asteroid.asteroid_movement()
    asteroid2.asteroid2_movement()
    asteroid3.asteroid3_movement()
    sprite_swordfish.update()
    screen.blit(puntuacion,(10,10))
    
    if lifes == 3:
        screen.blit(life_3,(700, 30))
    if lifes == 2:
        screen.blit(life_2,(700, 30))
    if lifes == 1:
        screen.blit(life_1,(700, 30))
    if lifes == 0:
        #game_over = True
        pass

    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.5
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        swordfish.go_up()
    if key[pg.K_DOWN]:
        swordfish.go_down()  
    pg.time.get_ticks()   
    sprite_swordfish.update()
    sprite_swordfish.draw(screen)

    asteroids_sprites.update()
    asteroids_sprites.draw(screen)
  
    if background_x <= final_mision1:
       background_x =  final_mision1
       screen.blit(mensaje_aterriza,(450,300))
    
    pg.time.get_ticks()
    pg.display.flip()
     


