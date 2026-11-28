import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler

class GameController:

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True
        #ajouté le 26/11 par Savvianna:
        self.selected_circuit = 0
        self.nb_circuits = 2

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):

        state = self.model.state

        if key == pygame.K_ESCAPE:

            if state == GameState.MENU:
                self.quit()

            elif state == GameState.RACING:
                self.model.state = GameState.CHOIX_CIRCUIT

            elif state == GameState.CHOIX_CIRCUIT:
                self.model.state = GameState.MENU

            return

        if state == GameState.MENU:

            if key == pygame.K_RETURN:
                self.model.state = GameState.CHOIX_CIRCUIT

        elif state == GameState.CHOIX_CIRCUIT:

            if key == pygame.K_LEFT:
                self.model.choisir_circuit(0)

            elif key == pygame.K_RIGHT:
                self.model.choisir_circuit(1)

            elif key == pygame.K_RETURN:
                self.model.load_circuit()

        elif state == GameState.RACING:

            # Après  victoire, Entrée 
            if (
                self.model.vainqueur is not None
                and key == pygame.K_RETURN
            ):
                self.model.state = GameState.CHOIX_CIRCUIT


    def update(self) -> None:
        if self.model.state != GameState.RACING:
            return
        # Ajout du 24/11 par Savvianna: pour utiliseur le dictionnaire de chaque joueur 
        inputs = self.input_handler.get_inputs()
        #modifié par Elina le 26/11: quand il y a pas de vainqueur le jeu continue
        if self.model.vainqueur is not None:
            return
        p1_input = inputs[0]
        p2_input = inputs[1]
        #ajouté le 24/11 par Savvianna
        car1 = self.model.car1
        car2 = self.model.car2
        self.apply_input(car1, p1_input)
        self.apply_input(car2, p2_input)
        self.model.update()
    #ajouté le 24/11 par Savvianna
    #par Luna:delete use item
    def apply_input(self, car, player_input) -> None:
        if player_input['accelerate']:
            car.accelerate()

        if player_input['brake']:
            car.brake()

        if player_input['turn_left']:
            car.turn_left()

        if player_input['turn_right']:
            car.turn_right()

    def render(self) -> None:
        self.view.draw(self.model)

    def quit(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()
