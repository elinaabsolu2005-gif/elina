import pygame
import math
#Modifié par Savvianna le 26/11: Import BOOST_ACCELERATION
#Modifié par Savvianna le 28/11: Import WINDOW_HEIGHT, WINDOW_WIDTH
from constants import (
CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, BOOST_ACCELERATION, WINDOW_HEIGHT, WINDOW_WIDTH
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()
        #modification par Elina le 26/11: Initialisation du nombre des tours de la derniere case
        #modification par Elina le 26/11: fixation de nombre des checkpoints qu'il faut valider
        self.derniere_case=None
        self.checkpoints_valides=set()
        #Luna:ajouter
        self.tours = 0

    #Modifié par Savvianna le 26/11: Quand la voiture passe par un boost elle accélère.
    def boost(self) -> None:
        self.speed += BOOST_ACCELERATION

    def brake(self) -> None:
        """ajoute par Luna 26/11"""
        self.speed = 0
        if self.speed > 200:
            self.marche_arriere()
        elif self.speed < 0:
            self.accelerate()

    def accelerate(self) -> None:
        self.speed += CAR_ACCELERATION

    def turn_right(self) -> None:
        """25/11 modifier par Luna :augmenter l'angle"""
        if self.angle > -360:
            self.angle -= 2
        else:
            self.angle = 0

    def turn_left(self) -> None:
            """25/11 modifier par Luna :augmenter l'angle"""
            if self.angle < 360:
                self.angle += 2
            else:
                self.angle = 0

    def update_position(self) -> None:
        """25/11 modifier par Luna :augmenter l'angle"""
        
        self.y += self.speed * math.cos(math.radians(self.angle))
        self.x -= self.speed * math.sin(math.radians(self.angle))


    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        #modification par Elina le 26/11: pare-brise gris
        pygame.draw.rect(surf,(220 ,240, 255),(5, 30, CAR_WIDTH-10, 10))
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect

    def _rester_dans_ecran(self):
        #Modifié par Elina:27/11 Faut rester dans les limites d'ecran, quand on arrive aux bords, il s'arrete
        #Modifié par Savvianna le 28/11: Ajout du le cas y
        marge_x = CAR_WIDTH / 2
        marge_y = CAR_HEIGHT / 2

        x = max(marge_x, min(WINDOW_WIDTH - marge_x, self.x))
        y = max(marge_y, min(WINDOW_HEIGHT - marge_y, self.y))

        if x != self.x or y != self.y:
            self.speed = 0.0

        self.x = x
        self.y = y
