import pygame
from settings import *
from support import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        self.image = image
        self.default_pos = pos
        self.rect = pygame.FRect(pos[0], pos[1], self.image.get_width() * SCALE, self.image.get_height() * SCALE)
        self.hitbox_rect = self.rect
        self.flip = False

    def get_direction_to_target(self, target : pygame.math.Vector2):
        if target != NotImplemented:
            return pygame.math.Vector2(target - pygame.math.Vector2(self.rect.centerx, self.rect.centery)).normalize()
        return pygame.math.Vector2(0, 0)

class PhysicsSprite(Sprite):
    def __init__(self, level, pos, image, groups):
        super().__init__(pos, image, groups)
        self.terrain_sprites = level.sprites["terrain"]
        self.velocity = vector(0, 0)
        self.speed = 4

    def move(self):
        if self.velocity != pygame.math.Vector2(0, 0):
            self.velocity = self.velocity.normalize()
        else:
            self.velocity = self.velocity

        self.hitbox_rect.x += self.velocity.x * +self.speed
        self.collide('horizontal')
        self.hitbox_rect.y += self.velocity.y * +self.speed
        self.collide('vertical')

        self.rect.center = self.hitbox_rect.center

    def collide(self, axis):
        for sprite in self.terrain_sprites:
            if self.hitbox_rect.colliderect(sprite.rect):
                if axis == 'horizontal':
                    if (self.velocity.x < 0):
                        self.hitbox_rect.left = sprite.rect.right
                    elif (self.velocity.x > 0):
                        self.hitbox_rect.right = sprite.rect.left
                elif axis == 'vertical':
                    if (self.velocity.y > 0):
                        self.hitbox_rect.bottom = sprite.rect.top
                    elif (self.velocity.y < 0):
                        self.hitbox_rect.top = sprite.rect.bottom

    def update(self):
        self.move()
    