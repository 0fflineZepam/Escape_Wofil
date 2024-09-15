import pygame as pg
import sys
from settings import *
from map import Map  # Upewnij się, że importujesz klasę Map bezpośrednio
from player import Player
from raycasting import *
from object_renderer import *




class Game:
    def __init__(self):
        # Inicjalizacja Pygame i ustawienia ekranu
        pg.init()
<<<<<<< HEAD
=======
        pg.mouse.set_visible(False)
>>>>>>> 62a09ed (sterowanie myszka podloga kolor wypelnienie ekranu niebieskie niebo)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)


    def update(self):
        # Aktualizacja ekranu i FPS
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        # Wypełnienie ekranu czarnym kolorem i rysowanie mapy
<<<<<<< HEAD
        self.screen.fill('black')
=======
        self.screen.fill('lightblue')
>>>>>>> 62a09ed (sterowanie myszka podloga kolor wypelnienie ekranu niebieskie niebo)
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        # Sprawdzenie zdarzeń (wyjście z gry przyciskiem Esc)
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        # Główna pętla gry
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()