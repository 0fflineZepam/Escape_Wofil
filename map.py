import pygame as pg

_ = False  # Definicja symbolicznej zmiennej dla pustego miejsca na mapie
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, _, _, _, _, 1, _, _, _, 4, _, _, _, _, _, 1, _, _, _, 1],
    [1, 1, _, 1, 1, 1, 1, _, 1, 1, 1, _, 1, 1, 1, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()  # Wczytaj mapę przy inicjalizacji

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        # Rysowanie prostokątów w miejscach, gdzie na mapie jest 1
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]