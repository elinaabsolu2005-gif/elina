import pygame
import math
#Modifié par Savvianna le 26/11: Import BOOST_ACCELERATION
from constants import (
CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE, BOOST_ACCELERATION
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()
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
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
