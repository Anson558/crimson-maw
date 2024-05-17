import pygame, sys
from pygame.math import Vector2 as vector

screen_size = (1280, 720)
display_size = (320, 180)
SCALE = 4
tile_size = 16 * SCALE

Z_LAYERS = {
    'decor': 2,
    'main': 5,
}