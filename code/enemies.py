from settings import *
from support import *
from sprites import *

class Enemy(PhysicsSprite):
    def __init__(self, level, pos, groups):
        self.animation = Animation(import_folder('images', 'entities', 'enemies', 'basic'), 7)
        self.image = self.animation.image
        super().__init__(level, pos, self.image, groups)
        self.speed = 2.8
        self.hitbox_rect = self.rect.inflate(-SCALE * 7, -SCALE * 4)
        self.level = level

    def update(self):
        super().update()
        self.check_death()
        self.animate()
        self.velocity = self.get_direction_to_target(self.level.player.rect.center)

    def check_death(self):
        for sprite in self.level.player_bullets:
            if self.rect.colliderect(sprite.rect):
                self.kill()

    def animate(self):
        self.animation.update()
        self.image = self.animation.image

        if self.velocity.x < 0:
            self.flip = True
        if self.velocity.x > 0:
            self.flip = False

