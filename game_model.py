from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile

circuit_1 =[
    """25/11 ajouté par Luna
    0:herbe, 1:road, 2:glace, 3:terre, 4:vide
    """
        [0,1,2,3,4,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

circuit_2 =[
        [0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]


class GameModel:
    """25/11 modifié par Luna(avec terrain)"""

    def __init__(self):
        self.state: str = GameState.MENU
        self.car: Car | None = None
        self.circuit = None
        self.circuits = []
        self.circuits_choisi = 0
        self.creer_circuit()

    def creer_circuit(self):
        grille1=[]
        for row in range(GRID_ROWS):
            ligne=[]
            for col in range(GRID_COLS):
                terrain = circuit_1[row][col]
                ligne.append(RoadTile(col,row,terrain))
            grille1.append(ligne)
        grille2=[]
        for row in range(GRID_ROWS):
            ligne=[]
            for col in range(GRID_COLS):
                terrain = circuit_2[row][col]
                ligne.append(RoadTile(col,row,terrain))
            grille2.append(ligne)
        self.circuits=[
            Circuit(grille1),
            Circuit(grille2)
        ]

    def choisir_circuit(self,num):
        self.circuits_choisi=num

    def load_circuit(self) -> None:
        self.circuit = self.circuits[self.circuits_choisi]
        self.spawn_car()
        self.state = GameState.RACING

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()

