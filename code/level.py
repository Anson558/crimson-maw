import pytmx
from settings import *
from support import *
from sprites import *
from player import *
from enemies import *
from groups import AllSprites
from os.path import join

class Level:
    def __init__(self):
        self.player_sprites = AllSprites(self)
        self.terrain_sprites = AllSprites(self)
        self.enemy_sprites = AllSprites(self)
        self.player_bullets = AllSprites(self)
        self.decor_sprites = AllSprites(self)

        self.map = pytmx.load_pygame(join('level.tmx'))
        self.setup()

        self.scroll = vector(0, 0)

        self.player = Player(
            level = self,
            pos = (900, 900),
            groups = self.player_sprites,
        )

        self.enemy = Enemy(
            level = self,
            pos = (1200, 1200),
            groups = self.enemy_sprites
        )

        # UI
        font = pygame.font.Font('slkscr.ttf', 30)
        self.start_text = font.render('Press Space to Start', False, (235, 220, 220))
        self.logo = import_image('images', 'logo')
        self.logo = pygame.transform.scale_by(self.logo, 5)

        # state
        self.game_state = 'menu'

    def update(self):
        self.apply_scroll()
        if self.game_state == 'game':
            self.player_bullets.update()
            self.player_sprites.update()
            self.enemy_sprites.update()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.game_state = 'menu'
        

    def setup(self):
        for x, y, image in self.map.get_layer_by_name('Terrain').tiles():
            Sprite((x * tile_size, y * tile_size), image, self.terrain_sprites)
        for x, y, image in self.map.get_layer_by_name('Decor').tiles():
            Sprite((x * tile_size, y * tile_size), image, self.decor_sprites)

    def draw(self):
        self.player_bullets.draw()
        self.player_sprites.draw()
        self.enemy_sprites.draw()
        self.terrain_sprites.draw()
        self.decor_sprites.draw()

        if self.game_state == 'menu':
            pygame.display.get_surface().fill((16, 20, 31))
            pygame.display.get_surface().blit(self.start_text, vector(pygame.display.get_window_size()[0]/2 - self.start_text.get_width()/2, pygame.display.get_window_size()[1]/2 + 55))
            pygame.display.get_surface().blit(self.logo, vector(pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])/2 - vector(self.logo.get_size()[0], self.logo.get_size()[1])/2)
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.game_state = 'game'

    def apply_scroll(self):
        self.scroll.x += (self.player.rect.centerx - pygame.display.get_surface().get_width()/2 - self.scroll.x)/18
        self.scroll.y += (self.player.rect.centery - pygame.display.get_surface().get_height()/2 - self.scroll.y)/18
