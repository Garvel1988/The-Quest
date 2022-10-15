
import pygame, random

class Aircraft(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Aircraft, self).__init__()
        self.image = pygame.image.load("images/aircraft/nave.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self._vy = 5  # The x-velocity.
       # self._spritex = pos[0]
        self._spritey = position[1]

    def go_up(self):
        # Update the _spritex position first and then the rect.
        self._spritey -= self._vy
        self.rect.centery = self._spritey

        if self.rect.centery < 40:
           self._spritey += self._vy


    def go_down(self):
        self._spritey += self._vy
        self.rect.centery = self._spritey

        if self.rect.centery > 550:
           self._spritey -= self._vy