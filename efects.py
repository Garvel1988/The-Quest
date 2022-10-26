import pygame as pg 
import random

class Sounds():
   def __init__(self):
     pg.mixer.init()
     self.expresions = [
        pg.mixer.Sound("Sounds/think.wav"),     
        pg.mixer.Sound("Sounds/alive.wav"),
        pg.mixer.Sound("Sounds/humble.wav")]

     self.ouch = [
    pg.mixer.Sound("Sounds/kick.wav"),     
    pg.mixer.Sound("Sounds/shame.wav"),
    pg.mixer.Sound("Sounds/point.wav")]      

     self.music_stage1 = pg.mixer.Sound("Sounds\Spiegel.wav")
     self.music_stage2 = pg.mixer.Sound("Sounds\Rush.wav")
     self.explosion = pg.mixer.Sound("Sounds\explosion.wav")
     self.music_congratulation = pg.mixer.Sound("Sounds/toogood.wav")
     self.turbosound = pg.mixer.Sound("Sounds/turbo_rocket.wav")


   def turbo(self):
       self.turbosound.set_volume(0.1)
       self.turbosound.play()

   def congratulation(self):
       self.music_congratulation.set_volume(0.1)
       self.music_congratulation.play()
    
   def switchoffcongratulation(self):
       pg.mixer.init()
       self.music_congratulation.set_volume(0.0)


   def play_explosion(self):
        self.explosion.set_volume(0.1)
        self.explosion.play()

   def play_explesion(self):
       self.expresions[random.randint(0,2)].play()

   def play_ouch(self):
       self.ouch[random.randint(0,2)].play()

   def play_music1(self):
     self.music_stage1.set_volume(0.1)
     self.music_stage1.play()

   def switchoffplay1(self):
    pg.mixer.init()
    self.music_stage1.set_volume(0.0)

   def switchoffplay2(self):
    pg.mixer.init()
    self.music_stage2.set_volume(0.0)

   def play_music2(self):
       self.music_stage2.set_volume(0.1)
       self.music_stage2.play()


class Swordfishchange():
    def __init__(self):
        self.swordfishcange = pg.image.load("images/aircraft/nave_imbencible.png") 

    def swordfishcangeimage(self):
        self.swordfishcange = pg.image.load("images/aircraft/nave_imbencible.png") 