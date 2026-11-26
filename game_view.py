
import pygame

from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    TILE_SIZE,
    COLOR_BG,
    COLOR_TEXT,
    COLOR_ACCENT,
    COLOR_PANEL,
    COLOR_PANEL_BORDER,
    GameState
)

from model.game_model import GameModel


class GameView:

    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont(
            "Arial", 24
        )

    def draw(self, model):

        self.screen.fill(COLOR_BG)

        if model.state == GameState.MENU:

            self._draw_menu(model)

        elif model.state == GameState.RACING:

            self._draw_racing(model)

        elif model.state == GameState.CHOIX_CIRCUIT:

            self._draw_selection(model)

        pygame.display.flip()

    def _draw_menu(self, model):

        cx = WINDOW_WIDTH // 2

        title = self.font.render(
            "Jeu de course 2D",
            True,
            COLOR_ACCENT
        )

        self.screen.blit(
            title,
            title.get_rect(center=(cx, 160))
        )

        options = [
            "JOUER (Enter)",
            "QUITTER (Escape)"
        ]

        for i, label in enumerate(options):

            y = 320 + i * 80

            rect = pygame.Rect(
                cx - 140,
                y - 25,
                280,
                50
            )

            pygame.draw.rect(
                self.screen,
                COLOR_PANEL,
                rect,
                border_radius=8
            )

            pygame.draw.rect(
                self.screen,
                COLOR_PANEL_BORDER,
                rect,
                2,
                border_radius=8
            )

            text = self.font.render(
                label,
                True,
                COLOR_ACCENT if i == 0 else COLOR_TEXT
            )

            self.screen.blit(
                text,
                text.get_rect(center=rect.center)
            )

    def _draw_selection(self, model):

        cx = WINDOW_WIDTH // 2

        title = self.font.render(
            "Choisis ton circuit",
            True,
            COLOR_ACCENT
        )

        self.screen.blit(
            title,
            title.get_rect(center=(cx, 150))
        )

        for i in range(2):

            x = cx - 170 + i * 200

            rect = pygame.Rect(
                x, 280, 140, 100
            )

            pygame.draw.rect(
                self.screen,
                COLOR_PANEL,
                rect
            )

            if model.circuit_choisi == i:

                pygame.draw.rect(
                    self.screen,
                    COLOR_ACCENT,
                    rect,
                    4
                )

            else:

                pygame.draw.rect(
                    self.screen,
                    COLOR_PANEL_BORDER,
                    rect,
                    2
                )

            texte = self.font.render(
                f"Circuit {i + 1}",
                True,
                COLOR_TEXT
            )

            self.screen.blit(
                texte,
                texte.get_rect(center=rect.center)
            )

        aide = self.font.render(
            "<- / -> pour choisir, Entree pour jouer",
            True,
            COLOR_TEXT
        )

        self.screen.blit(
            aide,
            aide.get_rect(center=(cx, 450))
        )

    def _draw_racing(self, model):

        if model.circuit is None:
            return

        # Afficher les cases du circuit
        for row_idx, row in enumerate(
            model.circuit.grid
        ):

            for col_idx, tile in enumerate(row):

                sprite = tile.get_sprite(TILE_SIZE)

                self.screen.blit(
                    sprite,
                    (
                        col_idx * TILE_SIZE,
                        row_idx * TILE_SIZE
                    )
                )

        # Afficher la voiture 1
        if model.car1 is not None:

            sprite, rect = (
                model.car1.get_rotated_sprite()
            )

            self.screen.blit(sprite, rect)

        # Afficher la voiture 2
        if model.car2 is not None:

            sprite, rect = (
                model.car2.get_rotated_sprite()
            )

            self.screen.blit(sprite, rect)

        # Modifie le 26/11 par Elina Afficher les compteurs de tours
        if model.car1 is not None:

            texte1 = self.font.render(
                f"Joueur 1 : {model.car1.tours} tours",
                True,
                COLOR_TEXT
            )

            self.screen.blit(
                texte1,
                (20, 20)
            )

        if model.car2 is not None:

            texte2 = self.font.render(
                f"Joueur 2 : {model.car2.tours} tours",
                True,
                COLOR_TEXT
            )

            self.screen.blit(
                texte2,
                (20, 50)
            )

        #Modifie le 26/11 par Elina  Afficher le gagnant
        if model.vainqueur is not None:

            if model.vainqueur == model.car1:

                message = "Joueur 1 a gagne !"

            else:

                message = "Joueur 2 a gagne !"

            texte = self.font.render(
                message,
                True,
                COLOR_ACCENT
            )

            self.screen.blit(
                texte,
                texte.get_rect(
                    center=(
                        WINDOW_WIDTH // 2,
                        100
                    )
                )
            )
