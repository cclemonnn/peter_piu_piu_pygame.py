import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("images/explosion1.png").convert())
        self.sprites.append(pygame.image.load("images/explosion2.png").convert())
        self.sprites.append(pygame.image.load("images/explosion3.png").convert())
        self.sprites.append(pygame.image.load("images/explosion4.png").convert())
        self.sprites.append(pygame.image.load("images/explosion5.png").convert())
        self.sprites.append(pygame.image.load("images/explosion6.png").convert())
        self.sprites.append(pygame.image.load("images/explosion7.png").convert())
        self.sprites.append(pygame.image.load("images/explosion8.png").convert())
        self.sprites.append(pygame.image.load("images/explosion9.png").convert())
        self.sprites.append(pygame.image.load("images/explosion10.png").convert())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect().move(x, y - 80)

    def update(self):
        self.current_sprite += 0.3
        if self.current_sprite > 9:
            self.kill()
        else:
            self.image = self.sprites[int(self.current_sprite)]
            self.image.set_colorkey((255, 255, 255))
