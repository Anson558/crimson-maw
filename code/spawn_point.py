from settings import *
from support import *
from enemies import *
from sprites import Sprite

class SpawnPoint(Sprite):
    def __init__(self, level, pos, groups):
        self.animation = Animation(import_folder('images', 'entities', 'enemies', 'spawn_point'), 30)
        self.image = self.animation.image
        super().__init__(pos, self.image, groups)
        self.level = level
        self.time_until_spawn = 260

    def update(self):
        self.animate()
        self.time_until_spawn -= 1
        if self.time_until_spawn <= 0:
            Enemy(
                level = self.level,
                pos = (self.rect.x, self.rect.y),
                groups = self.level.sprites['enemies']
            )
            self.kill()

    def animate(self):
        self.animation.update()
        self.image = self.animation.image
