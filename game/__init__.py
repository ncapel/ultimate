import pygame
import sys
from game.camera import CameraGroup
from game.tileset import Tileset
from game.player import Player

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        self.clock  = pygame.time.Clock()
        self.bg_color = pygame.Color('pink')
        self.camera = CameraGroup()
        self.tiles = Tileset('assets/gfx/Overworld.png', 16, 16, 36, 40)
        self.player = Player((640,360),self.camera)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
        # self.tiles.draw(self.screen) -- This draws the entire tileset
        # self.screen.blit(self.tiles.get_tile(0, 0), (72,72))  -- This draws a single tile at specified coordinates
        self.camera.update()
        self.camera.custom_draw(self.player)
        pygame.display.update()
        pygame.display.flip()