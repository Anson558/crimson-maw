from settings import *
from sprites import *

class PlayerBullet(Sprite):
    def __init__(self, level, pos, groups):
        self.level = level
        self.image = import_image('images', 'entities', 'player_bullet')
        super().__init__(pos, self.image, groups)
        speed = 12
        self.velocity = self.get_direction_to_target(vector(pygame.mouse.get_pos()[0] + level.scroll.x, pygame.mouse.get_pos()[1] + level.scroll.y)) * speed

    def update(self):
        super().update()
        self.rect.topleft += self.velocity
        for sprite in self.level.terrain_sprites:
            if self.rect.colliderect(sprite.rect):
                self.kill()