from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def draw(self):
        for sprite in self:
            pygame.display.get_surface().blit(
                pygame.transform.flip(pygame.transform.scale_by(sprite.image, SCALE), sprite.flip, False),
                sprite.rect.topleft - self.level.scroll
            )