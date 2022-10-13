import pygame as pg
from objects import Sprite

pg.mixer.init()
pg.init()
screen = pg.display.set_mode((1000,600))
pg.display.set_caption("The Quest")
background_image  = pg.image.load("images\planets\small.png").convert() #1.25 finalizar pantalla
background_x = 0
background_y =0
icon = pg.image.load("images\icon.PNG")
pg.display.set_icon(icon)
BLACK = pg.Color('black')

music = pg.mixer.Sound("Sounds\Rush.wav")
music.set_volume(0.1)
time_clock = pg.time.Clock()
#nave = aircraft(20,300, w=30, h=50,color=(229,190,1))
#nave.vy = 5
game_over = False
sprite = Sprite([100, 300])
active_sprite_list = pg.sprite.Group()
active_sprite_list.add(sprite)



#nave = pg.image.load("starcraft.PNG")#
music.play()
while not game_over:
   # pg.mixer.Sound.play(sonido_fondo)
    dt = time_clock.tick(50)
    screen.blit(background_image,(background_x,background_y,))
    for event in pg.event.get():
        if event.type == pg.QUIT:
          game_over = True
    background_x -= 0.3
    key = pg.key.get_pressed()
    # Use pygame.K_RIGHT etc. as the index.
    if key[pg.K_UP]:
        sprite.go_up()
    if key[pg.K_DOWN]:
        sprite.go_down()  # Not implemented.

    # Update the game.
    # This calls the update methods of all contained sprites.
    active_sprite_list.update()

    # Draw everything.
    #screen.fill(BLACK)
    # This blits the images of all sprites at their rect.topleft coords.
    active_sprite_list.draw(screen)

    pg.display.flip()
    
    pg.display.flip()
