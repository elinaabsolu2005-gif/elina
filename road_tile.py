import pygame
from constants import TILE_SIZE

class RoadTile:
    """25/11 commit par Luna"""

    def __init__(self, col: int, row: int, terrain: int):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None
        self.terrain = terrain

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        
        couleur =(80, 80, 90)
        if self.terrain == 0:
            self.sprite = None
            couleur = (50, 150, 70) #grasse
        elif self.terrain == 1:
            self.sprite = None
            couleur = (80, 80, 90) #road
        elif self.terrain == 2:
            self.sprite = None
            couleur = (165, 215, 240) #glacce
        elif self.terrain == 3:
            self.sprite = None
            couleur = (160, 110, 65) #terre
        elif self.terrain == 4:
            self.sprite = None
            couleur = (20, 20, 30) #vide


        surface.fill(couleur)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
