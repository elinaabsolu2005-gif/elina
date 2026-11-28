import pygame
from constants import TILE_SIZE

class RoadTile:
    """25/11 commit par Luna"""

    #Modifié le 26/11 par Savvianna: ajout de la paramètre bloc
    def __init__(self, col: int, row: int, terrain: int, block = None,type="route",checkpoint_id=None):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None
        self.terrain = terrain
        self.block = block
        self.type= type
        self.checkpoint_id = checkpoint_id

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

        #Modifié le 26/11 par Savvianna: ajout du 'B' en blanc si la cas est un Boost
        if self.block =='boost':
            police = pygame.font.SysFont(None, 36)
            lettre = police.render('B', True, (255, 255, 255))
            surface.blit(lettre,(24, 20))
        #Modifié le 26/11 par Savvianna: Ajout 1 ou 2 sur les cases du départ
        if self.block =='1' or self.block == '2':
            police = pygame.font.SysFont(None, 36)
            chiffre = police.render(self.block, True, (255, 255, 255))
            surface.blit(chiffre,(24, 20))
        # Couleur selon le type de case
        if self.type == "checkpoint":
            surface.fill((40, 160, 80))

        elif self.type == "finish":
            surface.fill((220, 190, 30))

        else:
            surface.fill((80, 80, 90))


        surface.fill(couleur)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
