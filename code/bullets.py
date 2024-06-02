from settings import *
from sprites import *
import random

class Bullet(Sprite):
    def __init__(self, level, pos, groups):
        self.level = level
        self.image = self.level.assets['enemy_bullet']
        super().__init__(pos, self.image, groups)
        self.speed = 3.5
        self.velocity = vector(0, 0)
        self.time_alive = 0

    def update(self):
        self.time_alive += 1
        super().update()
        self.rect.topleft += self.velocity * self.speed
        if self.time_alive >= 800:
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
        self.image = self.level.assets['player_bullet']
        self.speed = 12
        self.velocity = self.get_direction_to_target(vector(pygame.mouse.get_pos()[0] + level.scroll.x, pygame.mouse.get_pos()[1] + level.scroll.y))