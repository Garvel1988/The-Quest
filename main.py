from time import sleep
from turtle import back
import pygame as pg, time
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3



pg.mixer.init()
pg.init()
      



screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")

#images
background_image  = pg.image.load("images\planets\small.png").convert() #1.20 finalizar pantalla
background_x = 0
background_y =0
icon = pg.image.load("images\icon.PNG")
pg.display.set_icon(icon)


#sounds
music = pg.mixer.Sound("Sounds\Rush.wav")
music.set_volume(0.1)
explosion = pg.mixer.Sound("Sounds\explosion.wav")
explosion.set_volume(0.1)
music.play()


time_clock = pg.time.Clock()
game_over = False

text = "Game Over"
fuente = pg.font.Font(None, 60)
mensaje = fuente.render(text, 1, (255, 255, 255))

swordfish = Aircraft([100, 300])

sprite_swordfish = pg.sprite.Group()
sprite_swordfish.add(swordfish)

asteroid=Asteroid() 
asteroid2 = Asteroid2()
asteroid3 = Asteroid3()
asteroids_sprites= pg.sprite.Group()
asteroids_sprites.add(asteroid,asteroid2,asteroid3)

#asteroid_list = pg.sprite.Group()

#puntuaje = fuente.render(tiempo, 1, (255, 255, 255))

current_time = 0
background_time = 0

while not game_over:
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y))
    background_time = pg.time.get_ticks() 
    asteroid.asteroid_movement()
    asteroid2.asteroid2_movement()
    asteroid3.asteroid3_movement()
    sprite_swordfish.update()

    tiempo = pg.time.get_ticks() 
    texto = fuente.render("Score: "+str(tiempo), True,(255, 255, 0))
    screen.blit(texto,(10,10))
    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.3
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
    current_time = pg.time.get_ticks()
    colision = pg.sprite.groupcollide(sprite_swordfish,asteroids_sprites,False,False)
    if colision and current_time <103862:
        swordfish.image = pg.image.load("images/aircraft/explosion.png")
        explosion.play()
        time_clock.tick(12)
        screen.blit(mensaje,(400,30))
    else:
        swordfish.image = pg.image.load("images/aircraft/nave.png") 
    if current_time > 103862:
       background_x = -1185.8999999999116
    
    print(background_x)
    print(current_time)
    pg.time.get_ticks()
    pg.display.flip()
     