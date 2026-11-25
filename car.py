import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

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
