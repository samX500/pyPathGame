import pyglet

from environment.ArenaFactory import ArenaFactory
from gui.MazeDrawer import MazeDrawer
from gui.ElementColor import ElementColor


class Gui(pyglet.window.Window):
    WALL_COLOR = (0, 0, 0, 1)
    EMPTY_COLOR = (1, 1, 1, 1)
    WINDOW_SIZE = (500, 500)
    BOARD_SIZE = (30, 30)
    TILE_SIZE = 20

    def __init__(self):
        super().__init__(width=self.WINDOW_SIZE[0], height=self.WINDOW_SIZE[0])
        self.__arena = ArenaFactory.build_random_arena(*self.BOARD_SIZE)
        self.__drawer = MazeDrawer(self.__get_element_color(), self.TILE_SIZE, self.BOARD_SIZE, self.WINDOW_SIZE)

    def __get_element_color(self):
        colors = ElementColor()
        colors.set_empty_color(self.EMPTY_COLOR)
        colors.set_wall_color(self.WALL_COLOR)
        return colors

    def on_draw(self):
        self.clear()
        self.__drawer.draw_arena(self.__arena)


def run():
    window = Gui()
    pyglet.app.run()
