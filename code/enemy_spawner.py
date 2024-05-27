from settings import *
from support import *
from spawn_point import *
import random

class EnemySpawner:
    def __init__(self, level):
        self.level = level
        
        self.spawn_cooldown = 120
        self.time_since_spawn = 0

    def update(self):
        self.time_since_spawn += 1
        if self.time_since_spawn > self.spawn_cooldown:
            self.time_since_spawn = 0
            SpawnPoint(
                level = self.level,
                pos = (random.randrange(940, 2890), random.randrange(973, 2300)),
                groups = self.level.sprites['spawn_points']
            )