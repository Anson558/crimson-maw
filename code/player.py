from settings import *
from sprites import *
from bullets import *

class Player(PhysicsSprite):
    def __init__(self, level, pos, groups):
        self.level = level
        self.animations = {
            'idle': Animation(self.level.assets['player_idle'], 20),
            'run': Animation(self.level.assets['player_run'], 6)
        }
        super().__init__(self.level, pos, self.animations['idle'].image, groups)
        self.hitbox_rect = self.rect.inflate(-SCALE * 5, -SCALE * 4)

        self.shoot_timer = 0
        self.shoot_cooldown = 13

    def input(self):
        self.shoot_timer += 1
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_d]:
            self.velocity.x = 1
            self.flip = False
        elif keys[pygame.K_a]:
            self.velocity.x = -1
            self.flip = True
        else:
            self.velocity.x = 0

        print(self.velocity)

        if keys[pygame.K_w]:
            self.velocity.y = -1
        elif keys[pygame.K_s]:
            self.velocity.y = 1
        else:
            self.velocity.y = 0

        if mouse[0]:
            if self.shoot_timer > self.shoot_cooldown:
                self.shoot_timer = 0
                PlayerBullet(self.level, self.rect.center, self.level.sprites["player_bullets"])

    def check_death(self):
        for enemy_types in [self.level.sprites['enemies'], self.level.sprites['enemy_bullets']]:
            for enemy_type in enemy_types:
                if self.hitbox_rect.colliderect(enemy_type.hitbox_rect):
                    self.rect.topleft = self.default_pos
                    self.hitbox_rect.topleft = self.default_pos
                    self.level.sprites['enemies'].empty()
                    self.level.sprites['spawn_points'].empty()
                    self.level.game_state = 'menu'
                
        
    def animate(self):
        if self.velocity == vector(0, 0):
            self.animations['idle'].update()
            self.image = self.animations['idle'].image
        else:
            self.animations['run'].update()
            self.image = self.animations['run'].image

    def update(self):
        print(self.rect.topleft)
        self.input()
        self.animate()
        self.check_death()
        super().update()