import pygame as pg
from objects import Aircraft, Asteroid, Asteroid2, Asteroid3


pg.mixer.init()
pg.init()

screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")

background_image  = pg.image.load("images\planets\small.png").convert() #1.20 finalizar pantalla
background_x = 0
background_y =0
icon = pg.image.load("images\icon.PNG")
pg.display.set_icon(icon)

music = pg.mixer.Sound("Sounds\Rush.wav")
music.set_volume(0.1)
time_clock = pg.time.Clock()
game_over = False



swordfish = Aircraft([100, 300])
sprite_swordfish = pg.sprite.Group()
sprite_swordfish.add(swordfish)

asteroid=Asteroid() 
asteroid2 = Asteroid2()
asteroid3 = Asteroid3()
asteroids_sprites= pg.sprite.Group()
asteroids_sprites.add(asteroid,asteroid2,asteroid3)




#asteroid_list = pg.sprite.Group()
"""
cantidad = random.randint(30,40)
for i in range(cantidad):
    asteroid=Asteroid([1000,random.randint(100,600)])
    active_sprite_list.add(asteroid)
"""


music.play()
while not game_over:
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y))
    #active_sprite_list.
    asteroid.asteroid_movement()
    asteroid2.update2()
    asteroid3.update2()
    sprite_swordfish.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.3
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        swordfish.go_up()
    if key[pg.K_DOWN]:
        swordfish.go_down()  
       
    sprite_swordfish.update()
    sprite_swordfish.draw(screen)

    asteroids_sprites.update()
    asteroids_sprites.draw(screen)

    pg.display.flip()
 
""""
colision = pg.sprite.groupcollide(asteroids_sprites,asteroids_sprites,sprite_swordfish, False)
    if colision:
       swordfish.image = pg.image.load("images/aircraft/nave.png")
"""