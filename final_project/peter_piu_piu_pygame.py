import sys

import pygame
from pygame import key
from pygame.sprite import Group, groupcollide
from pygame.time import Clock

import settings
from final_project.antagonists import Meteor, UFO, Monster
from final_project.explosion import Explosion
from final_project.ground import Ground
from final_project.missile import Missile
from final_project.player import Player
from final_project.viewport import Viewport

# the main game pppp
class Game:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Peter Piu Piu Pygame")
        self.player = Player()
        self.player_group = Group()
        self.player_group.add(self.player)
        self.meteor_group = Group()
        # creates 20 meteor
        for i in range(20):
            meteor = Meteor()
            self.meteor_group.add(meteor)
        self.missile_group = Group()
        self.static_sprites = Group()
        self.static_sprites.add(Ground())
        self.viewport = Viewport()
        self.viewport.update(self.player)
        self.ufo_group = Group()
        # creates 5 ufo
        for i in range(5):
            ufo = UFO()
            self.ufo_group.add(ufo)
        self.monster_group = Group()
        # creates 7 monsters
        for i in range(7):
            monster = Monster()
            self.monster_group.add(monster)
        self.explosion_group = Group()
        pygame.init()
        self.font_arial = pygame.font.match_font('arial')
        self.font_bold = pygame.font.match_font('arial', bold=True)
        self.score = 0
        self.game_start = False

    def game_loop(self):
        clock = Clock()
        while True:
            self.handle_events()
            self.draw()
            self.update()
            self.show_instruction()
            self.show_score()
            self.show_level()
            if not self.game_start:
                self.restart_game()
                self.show_pppp()
                self.show_start_at_medium()
                self.show_start_at_hard()
            pygame.display.flip()
            clock.tick(settings.FPS)

    def show_instruction(self):
        font = pygame.font.Font(self.font_arial, 20)
        instruction = font.render("Press left or right key to move. Press space to shoot.", True, settings.WHITE)
        instruction_rect = instruction.get_rect()
        instruction_rect.left = 10
        instruction_rect.top = 10
        self.screen.blit(instruction, instruction_rect)

    def show_score(self):
        font = pygame.font.Font(self.font_arial, 30)
        score = font.render("Score: " + str(self.score), True, settings.AQUA)
        score_rect = score.get_rect()
        score_rect.left = 10
        score_rect.bottom = 70
        self.screen.blit(score, score_rect)

    def show_level(self):
        font = pygame.font.Font(self.font_arial, 30)
        if self.score < 150:
            level = font.render("Level: Medium (Score < 150)", True, settings.GREEN_YELLOW)
        else:
            level = font.render("Level: Hard (Score >= 150)", True, settings.ORANGE_RED)
        level_rect = level.get_rect()
        level_rect.left = 10
        level_rect.top = 80
        self.screen.blit(level, level_rect)

    def show_pppp(self):
        font = pygame.font.Font(self.font_bold, 100)
        game_over = font.render("PETER PIU PIU PYGAME", False, settings.AQUA_MARINE)
        game_over_rect = game_over.get_rect()
        game_over_rect.centerx = settings.WINDOW_WIDTH / 2
        game_over_rect.bottom = settings.WINDOW_HEIGHT / 2
        self.screen.blit(game_over, game_over_rect)

    def show_start_at_medium(self):
        font = pygame.font.Font(self.font_bold, 30)
        restart = font.render("Press \"1\" to start the game at Medium Level", True, settings.GREEN_YELLOW)
        restart_rect = restart.get_rect()
        restart_rect.centerx = settings.WINDOW_WIDTH / 2
        restart_rect.top = 20 + settings.WINDOW_HEIGHT / 2
        self.screen.blit(restart, restart_rect)

    def show_start_at_hard(self):
        font = pygame.font.Font(self.font_bold, 30)
        restart = font.render("Press \"2\" to start the game at Hard Level", True, settings.ORANGE_RED)
        restart_rect = restart.get_rect()
        restart_rect.centerx = settings.WINDOW_WIDTH / 2
        restart_rect.top = 60 + settings.WINDOW_HEIGHT / 2
        self.screen.blit(restart, restart_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if self.game_start:
                    if event.key == pygame.K_SPACE:
                        self.missile_group.add(Missile(self.player.rect.centerx, self.player.rect.top))

    def restart_game(self):
        keys = key.get_pressed()
        if keys[pygame.K_1]:
            self.start_at_medium()
        elif keys[pygame.K_2]:
            self.start_at_hard()

    def start_at_hard(self):
        self.game_start = True
        self.score = 150
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

    def start_at_medium(self):
        self.game_start = True
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
        if self.game_start:
            self.player_group.update()
        self.ufo_group.update()
        if self.score >= 150:
            self.monster_group.update()
        self.meteor_group.update()
        self.missile_group.update()
        self.viewport.update(self.player)
        if self.game_start:
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
            self.game_start = False
        player_ufo_collisions = groupcollide(self.player_group, self.ufo_group, True, True)
        for collision in player_ufo_collisions:
            self.explosion_group.add(Explosion(self.player.rect.x, self.player.rect.top))
            self.game_start = False
        player_monster_collisions = groupcollide(self.player_group, self.monster_group, True, True)
        for collision in player_monster_collisions:
            self.explosion_group.add(Explosion(self.player.rect.x, self.player.rect.top))
            self.game_start = False

    def draw(self):
        self.viewport.update_rect(self.static_sprites)
        self.viewport.update_rect(self.player_group)
        self.viewport.update_rect(self.meteor_group)
        self.viewport.update_rect(self.ufo_group)
        self.viewport.update_rect(self.monster_group)
        self.static_sprites.draw(self.screen)
        if self.game_start:
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
