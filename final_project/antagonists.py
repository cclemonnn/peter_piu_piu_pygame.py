import random

import pygame
from pygame.sprite import Sprite

from final_project import settings


class Meteor(Sprite):
    def __init__(self):
        super().__init__()
        # meteor image width: 50, height: 50
        self.image = pygame.image.load("images/meteor.png").convert_alpha()
        # self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()
        self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
        self.world_rect.bottom = random.randint(-80, 0)
        self.vertical_speed = random.randint(3, 5)
        self.horizontal_speed = random.randint(-3, 3)

    def update(self):
        self.world_rect.bottom += self.vertical_speed
        self.world_rect.left += self.horizontal_speed
        if self.world_rect.top > settings.WINDOW_HEIGHT or self.world_rect.left > settings.WORLD_WIDTH \
                or self.world_rect.right < 0:
            self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
            self.world_rect.bottom = random.randint(-80, 0)
            self.vertical_speed = random.randint(3, 5)
            self.horizontal_speed = random.randint(-3, 3)


class UFO(Sprite):
    def __init__(self):
        super().__init__()
        # UFO image width: 70, height: 70
        self.image = pygame.image.load("images/ufo.png").convert_alpha()
        # self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()
        self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
        self.world_rect.bottom = random.randint(-80, 0)
        self.vertical_speed = random.randint(5, 15)

    def update(self):
        self.world_rect.bottom += self.vertical_speed
        if self.world_rect.top > settings.WINDOW_HEIGHT:
            self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
            self.world_rect.bottom = random.randint(-80, 0)
            self.vertical_speed = random.randint(5, 15)


class Monster(Sprite):
    def __init__(self):
        super().__init__()
        # Monster image width: 100, height: 76
        self.sprites = []
        self.sprites.append(pygame.image.load("images/monster_left.png").convert_alpha())
        self.sprites.append(pygame.image.load("images/monster_right.png").convert_alpha())
        self.image = self.sprites[1]
        # self.image.set_colorkey((0, 0, 0))
        self.world_rect = self.image.get_rect()
        self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
        self.world_rect.bottom = random.randint(-80, 0)
        self.vertical_speed = random.randint(3, 6)
        self.horizontal_speed = random.randint(3, 6)

    def update(self):
        self.world_rect.bottom += self.vertical_speed
        if self.world_rect.bottom < 200:
            self.image = self.sprites[1]
            # self.image.set_colorkey((0, 0, 0))
            self.world_rect.left += self.horizontal_speed
        elif 200 <= self.world_rect.bottom < 400:
            self.image = self.sprites[0]
            # self.image.set_colorkey((0, 0, 0))
            self.world_rect.left += self.horizontal_speed * -1
        elif 400 <= self.world_rect.bottom < 600:
            self.image = self.sprites[1]
            # self.image.set_colorkey((0, 0, 0))
            self.world_rect.left += self.horizontal_speed
        else:
            self.image = self.sprites[0]
            # self.image.set_colorkey((0, 0, 0))
            self.world_rect.left += self.horizontal_speed * -1

        if self.world_rect.top > settings.WINDOW_HEIGHT or self.world_rect.left > settings.WORLD_WIDTH \
                or self.world_rect.right < 0:
            self.world_rect.left = random.randint(0, settings.WORLD_WIDTH - self.world_rect.width)
            self.world_rect.bottom = random.randint(-80, 0)
            self.vertical_speed = random.randint(3, 6)
            self.horizontal_speed = random.randint(3, 6)