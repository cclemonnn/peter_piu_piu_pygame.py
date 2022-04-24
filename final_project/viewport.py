"""calculates the location of each sprite object on screen"""


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