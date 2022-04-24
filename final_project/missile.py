import pygame
from pygame.sprite import Sprite

"""missile from spaceship"""


class Missile(Sprite):
    def __init__(self, x, y):
        super().__init__()
        # missile image width: 17, height: 40
        self.image = pygame.image.load("images/missile.png").convert_alpha()
        # self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.vertical_speed = -15

    def update(self):
        self.rect.bottom += self.vertical_speed
        if self.rect.bottom < 0:
            self.kill()