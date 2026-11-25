import pygame
from constants import TILE_SIZE
"""25/11 modifié par Luna"""
class RoadTile:

    def __init__(self, col: int, row: int, terrain: int):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None
        self.terrain = terrain

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        #surface.fill((80, 80, 90))
        
        couleur =(80, 80, 90)
        if self.terrain == 0:
            self.sprite = None
            couleur = (50,150,70) #grasse
        elif self.terrain == 1:
            self.sprite = None
            couleur = (80, 80, 90) #road
        elif self.terrain == 2:
            self.sprite = None
            couleur = (50, 120, 200) #water

        surface.fill(couleur)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
