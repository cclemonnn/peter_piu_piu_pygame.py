import pygame
from pygame import key

from pygame.sprite import Sprite

import settings
"""spaceship controlled by the player"""


class Player(Sprite):
    def __init__(self):
        super().__init__()
        # ship image width: 80, height: 120
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        # take out the background color, which is black, in the player image
        # self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect().move(2073, 650)

    def update(self):
        keys = key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.world_rect.left > 50:
                self.world_rect.left -= 20
        if keys[pygame.K_RIGHT]:
            if self.world_rect.right < settings.WORLD_WIDTH - 50:
                self.world_rect.right += 20
