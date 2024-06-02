from settings import *
from sprites import *
import random

class Bullet(Sprite):
    def __init__(self, level, pos, groups):
        self.level = level
        self.image = import_image('images', 'entities', 'enemy_bullet')
        super().__init__(pos, self.image, groups)
        self.speed = 3.5
        self.velocity = vector(0, 0)

    def update(self):
        super().update()
        self.rect.topleft += self.velocity * self.speed
        for sprite in self.level.sprites["terrain"]:
            if self.rect.colliderect(sprite.rect):
                self.kill()

class ShooterBullet(Bullet):
    def __init__(self, level, pos, groups):
        super().__init__(level, pos, groups)
        self.velocity = vector(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

class SniperBullet(Bullet):
    def __init__(self, level, pos, groups):
        super().__init__(level, pos, groups)
        self.velocity = self.get_direction_to_target(vector(self.level.player.rect.centerx, self.level.player.rect.centery))

class PlayerBullet(Bullet):
    def __init__(self, level, pos, groups):
        super().__init__(level, pos, groups)
        self.image = import_image('images', 'entities', 'player_bullet')
        self.speed = 12
        self.velocity = self.get_direction_to_target(vector(pygame.mouse.get_pos()[0] + level.scroll.x, pygame.mouse.get_pos()[1] + level.scroll.y))