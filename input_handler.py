import pygame


PLAYER1_MAPPING = {

    # Joueur 1
    pygame.K_z: "accelerate",
    pygame.K_w: "accelerate",
    pygame.K_s: "brake",
    pygame.K_q: "turn_left",
    pygame.K_a: "turn_left",
    pygame.K_d: "turn_right",
    pygame.K_SPACE: "use_item"
}


PLAYER2_MAPPING = {    # Joueur 2
    pygame.K_UP: "accelerate",
    pygame.K_DOWN: "brake",
    pygame.K_LEFT: "turn_left",
    pygame.K_RIGHT: "turn_right",
    pygame.K_RETURN: "use_item"
}

PLAYERS_MAPPING = [PLAYER1_MAPPING, PLAYER2_MAPPING]


class InputHandler:
    """C'est une classe pour gérer les commandes que les joueurs utilisent"""
    
    def __init__(self):
        self.mappings = PLAYERS_MAPPING

    def get_inputs(self) -> list[dict]:
        """Lit les touches appuyeés au clavier et renvoie une liste des 2 dictionnaires qu'elle contient pour chaque action si elle est demandée ou pas(True, False)."""
        keys = pygame.key.get_pressed()
        inputs = []
        for mapping in self.mappings:
            p = {action: False for action in mapping.values()} 
            for key, action in mapping.items(): 
                if keys[key]:
                    p[action] = True

            inputs.append(p)
        return inputs


