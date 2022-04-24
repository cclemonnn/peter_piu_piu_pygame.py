import pygame
from pygame.sprite import Sprite

import settings
"""background of the game"""


class Ground(Sprite):
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load("images/ground.png").convert()
        self.image = pygame.transform.scale(self.ground, (settings.WORLD_WIDTH, settings.WINDOW_HEIGHT))
        self.world_rect = self.image.get_rect().copy()
        self.world_rect.bottom = settings.WINDOW_HEIGHT