import pygame as pg,random
from objects import Aircraft, Asteroid

pg.mixer.init()
pg.init()
screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")
background_image  = pg.image.load("images\planets\small.png").convert() #1.20 finalizar pantalla
background_x = 0
background_y =0
icon = pg.image.load("images\icon.PNG")
pg.display.set_icon(icon)
#BLACK = pg.Color('black')

music = pg.mixer.Sound("Sounds\Rush.wav")
music.set_volume(0.0)
time_clock = pg.time.Clock()

game_over = False


nave = Aircraft([100, 300])


asteroid=Asteroid([1000,random.randint(100,600)]) #posicion aleatoria
#asteroid = Asteroid([900,300])
active_sprite_list = pg.sprite.Group()
active_sprite_list.add(nave,asteroid)




music.play()
while not game_over:
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y,))
    asteroid.asteroid_movement()
    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.3
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        nave.go_up()
    if key[pg.K_DOWN]:
        nave.go_down()  
    active_sprite_list.update()
    active_sprite_list.draw(screen)
    
    

    pg.display.flip()
    
