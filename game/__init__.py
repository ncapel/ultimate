import pygame
import sys
from game.tileset import Tileset

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280,640))
        self.clock  = pygame.time.Clock()
        self.bg_color = pygame.Color('black')
        self.tiles = Tileset('assets/gfx/Overworld.png', 16, 16, 36, 40)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
        self.tiles.draw(self.screen)
        pygame.display.flip()