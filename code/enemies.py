from settings import *
from support import *
from sprites import *

class Enemy(PhysicsSprite):
    def __init__(self, level, pos, groups):
        self.level = level
        self.animation = Animation(import_folder('images', 'entities', 'enemies', 'basic'), 14)
        self.image = self.animation.image
        super().__init__(level, pos, self.image, groups)
        self.speed = 1

        # hitbox
        self.hitbox_rect = self.rect.inflate(-SCALE * 7, -SCALE * 4)
        self.hit_cooldown = 15
        self.time_since_hit = 0
        self.health = 4

    def update(self):
        super().update()
        self.check_death()
        self.animate()
        self.velocity = self.get_direction_to_target(self.level.player.rect.center)
        print(self.velocity)

    def check_death(self):
        self.time_since_hit += 1
        for sprite in self.level.sprites["player_bullets"]:
            if self.rect.colliderect(sprite.rect):
                if self.time_since_hit >= self.hit_cooldown:
                    self.time_since_hit = 0
                    self.health -= 1
        
        if self.health <= 0:
            self.kill()

    def animate(self):
        self.animation.update()
        self.image = self.animation.image

        if self.velocity.x < 0:
            self.flip = True
        if self.velocity.x > 0:
            self.flip = False

class ShootingEnemy:
    def __init__(self, level, pos, groups):
        self.level = level

