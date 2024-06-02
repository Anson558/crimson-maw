import pytmx
from settings import *
from support import *
from sprites import *
from player import *
from enemies import *
from enemy_spawner import *
from groups import AllSprites
from os.path import join

class Level:
    def __init__(self):
        self.level_background = import_image("images/background")

        self.assets = {
            'player_idle': import_folder('images', 'entities', 'player', 'idle'),
            'player_run': import_folder('images', 'entities', 'player', 'run'),
            'basic_enemy': import_folder('images', 'entities', 'enemies', 'basic'),
            'shooting_enemy': import_folder('images', 'entities', 'enemies', 'shooter'),
            'player_bullet': import_image('images', 'entities', 'player_bullet'),
            'enemy_bullet': import_image('images', 'entities', 'enemy_bullet')
        }

        self.sprites = {
            "player": AllSprites(self),
            "terrain": AllSprites(self),
            "enemies": AllSprites(self),
            "spawn_points": AllSprites(self),
            "player_bullets": AllSprites(self),
            "enemy_bullets": AllSprites(self),
            "decor": AllSprites(self)
        }

        self.enemy_spawner = EnemySpawner(self)

        self.map = pytmx.load_pygame(join('level.tmx'))
        self.setup()

        self.scroll = vector(0, 0)

        self.player = Player(
            level = self,
            pos = (900, 900),
            groups = self.sprites["player"],
        )

        font = pygame.font.Font('slkscr.ttf', 30)
        self.start_text = font.render('Press Space to Start', False, (235, 220, 220))
        self.logo = import_image('images', 'logo')
        self.logo = pygame.transform.scale_by(self.logo, 5)

        self.game_state = 'menu'

    def update(self):
        self.apply_scroll()
        if self.game_state == 'game':
            self.enemy_spawner.update()

            self.sprites["enemies"].update()
            self.sprites["spawn_points"].update()
            self.sprites["player"].update()
            self.sprites["enemies"].update()
            self.sprites["player_bullets"].update()
            self.sprites["enemy_bullets"].update()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.game_state = 'menu'
        

    def setup(self):
        for x, y, image in self.map.get_layer_by_name('Terrain').tiles():
            Sprite((x * tile_size, y * tile_size), image, self.sprites["terrain"])
        for x, y, image in self.map.get_layer_by_name('Decor').tiles():
            Sprite((x * tile_size, y * tile_size), image, self.sprites["decor"])

        for sprite in self.sprites["terrain"]:
            self.level_background.blit(
                pygame.transform.flip(pygame.transform.scale_by(sprite.image, SCALE), sprite.flip, False),
                sprite.rect.topleft
            )
        for sprite in self.sprites["decor"]:
            self.level_background.blit(
                pygame.transform.flip(pygame.transform.scale_by(sprite.image, SCALE), sprite.flip, False),
                sprite.rect.topleft
            )

    def draw(self):
        pygame.display.get_surface().blit(self.level_background, -self.scroll)
        self.sprites["enemies"].draw()
        self.sprites["spawn_points"].draw()
        self.sprites["player_bullets"].draw()
        self.sprites["enemy_bullets"].draw()
        self.sprites["player"].draw()
        self.sprites["enemies"].draw()

        if self.game_state == 'menu':
            pygame.display.get_surface().fill((16, 20, 31))
            pygame.display.get_surface().blit(self.start_text, vector(pygame.display.get_window_size()[0]/2 - self.start_text.get_width()/2, pygame.display.get_window_size()[1]/2 + 55))
            pygame.display.get_surface().blit(self.logo, vector(pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])/2 - vector(self.logo.get_size()[0], self.logo.get_size()[1])/2)
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.game_state = 'game'

    def apply_scroll(self):
        self.scroll.x += (self.player.rect.centerx - pygame.display.get_surface().get_width()/2 - self.scroll.x)/18
        self.scroll.y += (self.player.rect.centery - pygame.display.get_surface().get_height()/2 - self.scroll.y)/18
