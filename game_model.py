from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile

circuit_1 =[
    # 25/11 ajouté par Luna
    # 0:herbe, 1:road, 2:glace, 3:terre, 4:vide
    #modifié le 25/11 par Savvianna: Modifications de valeurs à l'interieur du circuit1
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,2,0,0,0,0,0,0,0,0,0,0,2,1,0],
        [0,1,2,2,0,0,0,0,0,0,0,0,0,2,1,0],
        [0,1,2,2,0,0,0,3,0,0,0,0,0,2,1,0],
        [0,1,2,2,0,0,3,3,3,0,0,0,0,2,1,0],
        [0,1,2,0,0,0,3,3,3,0,0,0,0,2,1,0],
        [0,1,2,0,0,0,0,0,4,4,4,4,0,2,1,0],
        [0,1,2,0,0,0,0,0,4,4,4,4,0,2,1,0],
        [0,1,2,0,0,0,0,0,0,4,0,0,0,2,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
#modifié le 28/11 par Elina : design du circuit 2 
circuit_2 = [
    [4,4,0,0,0,0,0,0,0,0,0,0,0,0,4,4],
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,1,2,1,0,0,0,0,0,1,2,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0],
    [0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [4,4,0,0,0,0,0,0,0,0,0,0,0,0,4,4],
    [4,4,4,0,0,0,0,0,0,0,0,0,0,4,4,4]
]

class GameModel:
    """25/11 modifié par Luna(avec terrain)"""

    def __init__(self):
        self.state: str = GameState.MENU
        self.car1: Car | None = None
        self.car2: Car | None = None
        self.circuit = None
        self.circuits = []
        self.circuits_choisi = 0
        self.creer_circuit()
        #Luna:ajouter
        self.vainqueur = None

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
        #Modifié par Elina le 28/11
        definitions = [
            [(4, 3), (6, 5)],
            [(3, 3), (5, 5)]
        ]

        self.circuits = []

        for checkpoints in definitions:

            grille = [
                [RoadTile(col, row) for col in range(GRID_COLS)]
                for row in range(GRID_ROWS)
            ]

            for numero, (col, row) in enumerate(checkpoints):

                grille[row][col] = RoadTile(
                    col, row,
                    type="checkpoint",
                    checkpoint_id=numero
                )

            # Arrivée sur 2 cases : une par joueur
            for col in (7, 8):

                grille[1][col] = RoadTile(
                    col, 1,
                    type="finish"
                )

            self.circuits.append(Circuit(grille, 3))


    def choisir_circuit(self,num):
        self.circuits_choisi=num

    #Modifié par Savvianna le 26/11: ajoute des deux blocs boost au circuit choisi et ajoute des cases de départ des 2 joueurs
    def load_circuit(self) -> None: 
        self.circuit = self.circuits[self.circuits_choisi]
        self.circuit.get_tile(5, 3).block = 'boost'
        self.circuit.get_tile(8, 6).block = 'boost'
        self.circuit.get_tile(7, 1).block = '1'
        self.circuit.get_tile(8, 1).block = '2'
        self.spawn_car()
        self.state = GameState.RACING

    def spawn_car(self) -> None:
        #Luna:
        self.car1 = Car(7, 1)
        self.car2 = Car(8, 1)
    #modifie par Elina le 28/11
    def verifier_bloc(self, car, tile):

        if tile is None:
            return

        if tile.type == "checkpoint":

            car.checkpoints_valides.add(tile.checkpoint_id)

        elif tile.type == "finish":

            tous_valides = set(
                self.circuit.checkpoints
            ).issubset(car.checkpoints_valides)

            if tous_valides:

                car.tours += 1

                car.checkpoints_valides.clear()

                if car.tours >= self.circuit.nombre_tours:
                    self.vainqueur = car

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car1.update_position()
        self.car2.update_position()
        #Modifié le 26/11 par Savvianna: regarder si le cas est un boost, la voiture accélère
        tile = self.circuit.get_tile_at_pixel(self.car1.x, self.car1.y)
        if tile is not None and tile.block == 'boost':
            self.car1.boost()
        tile = self.circuit.get_tile_at_pixel(self.car2.x, self.car2.y)
        if tile is not None and tile.block == 'boost':
            self.car2.boost()
        #modifié par Elina le 28/11
        for car in [self.car1, self.car2]:

            if car is None:
                continue

            if self.vainqueur is not None:
                return

            ancienne_x = car.x
            ancienne_y = car.y

            car.update_position()

            # Vérifier les cases traversées
            distance = math.hypot(
                car.x - ancienne_x,
                car.y - ancienne_y
            )

            nombre_etapes = max(1, int(distance / 5))

            for i in range(1, nombre_etapes + 1):

                ratio = i / nombre_etapes

                x = ancienne_x + (car.x - ancienne_x) * ratio
                y = ancienne_y + (car.y - ancienne_y) * ratio

                tile = self.circuit.get_tile_at_pixel(x, y)

                if tile is None:
                    continue

                position_case = (tile.col, tile.row)

                if position_case != car.derniere_case:

                    car.derniere_case = position_case

                    self.verifier_bloc(car, tile)

