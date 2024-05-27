from settings import *
from support import *
from level import Level

class Main:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(screen_size, vsync=1)
        pygame.display.set_caption('Crimson Maw')

        self.clock = pygame.time.Clock()
        self.level = Level()

    def update(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.level.update()
            self.level.draw()

            pygame.display.update()

Main().update()
