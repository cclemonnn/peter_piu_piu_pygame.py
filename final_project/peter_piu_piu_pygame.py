import random
import sys

import pygame
from pygame import key
from pygame.sprite import Sprite, Group, groupcollide
from pygame.time import Clock

import settings


class Ground(Sprite):
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load("images/ground.png").convert()
        self.image = pygame.transform.scale(self.ground, (settings.WORLD_WIDTH, settings.WINDOW_HEIGHT))
        self.world_rect = self.image.get_rect().copy()
        self.world_rect.bottom = settings.WINDOW_HEIGHT


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


class Missile(Sprite):
    def __init__(self, x, y):
        super().__init__()
        # missile image width: 17, height: 40
        self.image = pygame.image.load("images/missile.png").convert_alpha()
        #self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.vertical_speed = -15

    def update(self):
        self.rect.bottom += self.vertical_speed
        if self.rect.bottom < 0:
            self.kill()


class Viewport:
    def __init__(self):
        self.left = 0

    def update(self, sprite):
        # WINDOW_WIDTH/2 - player surface/2 = 472
        # WORLD_WIDTH - 472 = 3624
        if sprite.world_rect.left > 472 and sprite.world_rect.right < 3624:
            self.left = sprite.world_rect.left - 472

    def update_rect(self, group):
        for sprite in group:
            sprite.rect = sprite.world_rect.move(-self.left, 0)


class Game:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Peter Piu Piu Pygame")
        self.player = Player()
        self.player_group = Group()
        self.player_group.add(self.player)
        self.meteor_group = Group()
        for i in range(20):
            meteor = Meteor()
            self.meteor_group.add(meteor)
        self.missile_group = Group()
        self.static_sprites = Group()
        self.static_sprites.add(Ground())
        self.viewport = Viewport()
        self.viewport.update(self.player)
        self.ufo_group = Group()
        for i in range(5):
            ufo = UFO()
            self.ufo_group.add(ufo)
        self.monster_group = Group()
        for i in range(7):
            monster = Monster()
            self.monster_group.add(monster)
        self.explosion_group = Group()
        pygame.init()
        self.font_arial = pygame.font.match_font('arial')
        self.font_bold = pygame.font.match_font('arial', bold=True)
        self.score = 0

    def game_loop(self):
        clock = Clock()
        while True:
            self.handle_events()
            self.draw()
            self.update()
            self.show_instruction()
            self.show_score()
            self.show_level()
            if not self.player.alive():
                self.restart_game()
                self.show_game_over()
                self.show_restart()
            pygame.display.flip()
            clock.tick(settings.FPS)

    def show_instruction(self):
        font = pygame.font.Font(self.font_arial, 20)
        instruction = font.render("Press left or right key to move. Press space to shoot.", True, (255, 255, 255))
        instruction_rect = instruction.get_rect()
        instruction_rect.left = 10
        instruction_rect.top = 10
        self.screen.blit(instruction, instruction_rect)

    def show_score(self):
        font = pygame.font.Font(self.font_arial, 30)
        score = font.render("Score: " + str(self.score), True, (0, 255, 255))
        score_rect = score.get_rect()
        score_rect.left = 10
        score_rect.bottom = 70
        self.screen.blit(score, score_rect)

    def show_level(self):
        font = pygame.font.Font(self.font_arial, 30)
        if self.score < 150:
            level = font.render("Level: Medium (Score < 150)", True, (173, 255, 47))
        else:
            level = font.render("Level: Hard (Score >= 150)", True, (255, 165, 0))
        level_rect = level.get_rect()
        level_rect.left = 10
        level_rect.top = 80
        self.screen.blit(level, level_rect)

    def show_game_over(self):
        font = pygame.font.Font(self.font_bold, 100)
        game_over = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over.get_rect()
        game_over_rect.centerx = settings.WINDOW_WIDTH / 2
        game_over_rect.bottom = settings.WINDOW_HEIGHT / 2
        self.screen.blit(game_over, game_over_rect)

    def show_restart(self):
        font = pygame.font.Font(self.font_bold, 30)
        restart = font.render("Press \"R\" to restart the game", True, (255, 215, 0))
        restart_rect = restart.get_rect()
        restart_rect.centerx = settings.WINDOW_WIDTH / 2
        restart_rect.top = 20 + settings.WINDOW_HEIGHT / 2
        self.screen.blit(restart, restart_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if self.player.alive():
                    if event.key == pygame.K_SPACE:
                        self.missile_group.add(Missile(self.player.rect.centerx, self.player.rect.top))

    def restart_game(self):
        keys = key.get_pressed()
        if keys[pygame.K_r]:
            self.score = 0
            self.player = Player()
            self.player_group = Group()
            self.player_group.add(self.player)
            self.meteor_group = Group()
            for i in range(20):
                meteor = Meteor()
                self.meteor_group.add(meteor)
            self.missile_group = Group()
            self.static_sprites = Group()
            self.static_sprites.add(Ground())
            self.viewport = Viewport()
            self.viewport.update(self.player)
            self.ufo_group = Group()
            for i in range(5):
                ufo = UFO()
                self.ufo_group.add(ufo)
            self.monster_group = Group()
            for i in range(5):
                monster = Monster()
                self.monster_group.add(monster)
            self.explosion_group = Group()

    def update(self):
        self.player_group.update()
        self.ufo_group.update()
        if self.score >= 150:
            self.monster_group.update()
        self.meteor_group.update()
        self.missile_group.update()
        self.viewport.update(self.player)
        self.check_player_collisions()
        self.check_collisions()
        if not self.player.alive():
            self.explosion_group.update()

    def check_collisions(self):
        meteor_collisions = groupcollide(self.meteor_group, self.missile_group, True, True)
        for collision in meteor_collisions:
            meteor = Meteor()
            self.meteor_group.add(meteor)
            self.score += 10
        ufo_collisions = groupcollide(self.ufo_group, self.missile_group, True, True)
        for collision in ufo_collisions:
            ufo = UFO()
            self.ufo_group.add(ufo)
            self.score += 30
        monster_collisions = groupcollide(self.monster_group, self.missile_group, True, True)
        for collision in monster_collisions:
            monster = Monster()
            self.monster_group.add(monster)
            self.score += 50

    def check_player_collisions(self):
        player_meteor_collisions = groupcollide(self.player_group, self.meteor_group, True, True)
        for collision in player_meteor_collisions:
            self.explosion_group.add(Explosion(self.player.rect.x, self.player.rect.top))
        player_ufo_collisions = groupcollide(self.player_group, self.ufo_group, True, True)
        for collision in player_ufo_collisions:
            self.explosion_group.add(Explosion(self.player.rect.x, self.player.rect.top))
        player_monster_collisions = groupcollide(self.player_group, self.monster_group, True, True)
        for collision in player_monster_collisions:
            self.explosion_group.add(Explosion(self.player.rect.x, self.player.rect.top))

    def draw(self):
        self.viewport.update_rect(self.static_sprites)
        self.viewport.update_rect(self.player_group)
        self.viewport.update_rect(self.meteor_group)
        self.viewport.update_rect(self.ufo_group)
        self.viewport.update_rect(self.monster_group)
        self.static_sprites.draw(self.screen)
        self.player_group.draw(self.screen)
        self.explosion_group.draw(self.screen)
        self.meteor_group.draw(self.screen)
        self.ufo_group.draw(self.screen)
        if self.score >= 150:
            self.monster_group.draw(self.screen)
        self.missile_group.draw(self.screen)
        self.explosion_group.draw(self.screen)


if __name__ == '__main__':
    Game().game_loop()