import pygame
import random

class Asteroid2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroids/asteroid1.png")
        self.rect = self.image.get_rect()
        self.rect.center = 1000,random.randint(100,600)
        self.speed = random.randint(8,15)
        
    def update2(self):
        self.rect.x -= self.speed

        if self.rect.left < -100:
            self._spritex=1100
            self._spritex -= self.speed
            self.rect.centerx = self._spritex
            self.rect.center = 1000,random.randint(100,600)
        