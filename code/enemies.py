from settings import *
from support import *
from sprites import *
from bullets import *

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
        self.can_flip = True

    def update(self):
        super().update()
        self.check_death()
        self.animate()
        self.move_toward_player()

    def move_toward_player(self):
        self.velocity = self.get_direction_to_target(self.level.player.rect.center)

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

        if self.can_flip:
            if self.velocity.x < 0:
                self.flip = True
            if self.velocity.x > 0:
                self.flip = False

class ShootingEnemy(Enemy):
    def __init__(self, level, pos, groups):
        self.level = level
        super().__init__(self.level, pos, groups)
        self.animation = Animation(import_folder('images', 'entities', 'enemies', 'shooter'), 14)
        self.time_since_shot = 0
        self.shoot_cooldown = 50
        self.can_flip = False

    def update(self):
        super().update()
        self.time_since_shot += 1
        if self.time_since_shot > self.shoot_cooldown:
            self.time_since_shot = 0
            ShooterBullet(
                level=self.level,
                pos=self.rect.center,
                groups=self.level.sprites['enemy_bullets']
            )

    def move(self):
        if vector(self.rect.x, self.rect.y).distance_to(vector(self.level.player.rect.x, self.level.player.rect.y)) > 400:
            super().move()

