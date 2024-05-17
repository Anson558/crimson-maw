from settings import *
from support import *
from level import Level

class Main:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
        pygame.display.set_caption('Crimson Maw')

        self.level = Level()
        self.clock = pygame.time.Clock()

    def update(self):
        while True:
            print(self.clock.get_fps())
            self.screen.fill((60, 70, 85))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.update()
            self.level.draw()

            pygame.display.update()
            self.clock.tick()

Main().update()
