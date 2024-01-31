import pygame

class Tilesheet:
    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load(filename).convert()
        self.tile_table = []
        for tile_x in  range(0, cols):
            line = []