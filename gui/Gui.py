import pickle

import pyglet
from pyglet.window import key

from environment.Arena import Arena
from environment.element.Element import Element
from environment.element.object.EmptySpace import EmptySpace
from environment.element.object.Wall import Wall
from gui.ElementColor import ElementColor
from gui.MazeDrawer import MazeDrawer
from pathFinder.PersonalPathFinder import PersonalPathFinder


class Gui(pyglet.window.Window):
    WALL_COLOR = (0, 0, 0, 1)
    EMPTY_COLOR = (1, 1, 1, 1)
    END_COLOR = (0, 1, 0, 1)
    BEGINNING_COLOR = (0, 0, 1, 1)
    PATH_COLOR = (0, 1, 1, 1)
    BOARD_SIZE = (30, 30)
    TILE_SIZE = 20
    WINDOW_SIZE = (BOARD_SIZE[0] * TILE_SIZE + 100, BOARD_SIZE[1] * TILE_SIZE + 100)

    ELEMENT_CHAR_SIZE = 20
    ELEMENT_CHAR_COLOR = (255, 0, 0, 255)

    def __init__(self):
        super().__init__(width=self.WINDOW_SIZE[0], height=self.WINDOW_SIZE[0])
        self.__arena = Arena(*self.BOARD_SIZE)
        self.__drawer = MazeDrawer(self.__get_element_color(), self.TILE_SIZE, self.BOARD_SIZE, self.WINDOW_SIZE,
                                   self.ELEMENT_CHAR_SIZE)
        self.__current_element = Element.WALL
        self.__beginning = None
        self.__end = None
        self.__path = None

    def __get_element_color(self):
        colors = ElementColor()
        colors.set_empty_color(self.EMPTY_COLOR)
        colors.set_wall_color(self.WALL_COLOR)
        colors.set_element_char_color(self.ELEMENT_CHAR_COLOR)
        colors.set_beginning_color(self.BEGINNING_COLOR)
        colors.set_ending_color(self.END_COLOR)
        colors.set_path_color(self.PATH_COLOR)
        return colors

    def on_draw(self):
        self.clear()
        self.__drawer.draw_current_element(self.__current_element)
        self.__drawer.draw_arena(self.__arena)
        if self.__path is not None:
            self.__drawer.draw_path(self.__path)

        if self.__beginning is not None:
            self.__drawer.draw_beginning(self.__beginning)
        if self.__end is not None:
            self.__drawer.draw__ending(self.__end)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        x, y = self.__drawer.get_mouse_position(x, y)
        if self.__arena.is_in_bound(x, y) and isinstance(self.__arena.get_element_at(x, y), EmptySpace):
            if self.__current_element == Element.BEGINNING:
                self.__beginning = x, y
                self.__path = None
            elif self.__current_element == Element.END:
                self.__end = x, y
                self.__path = None

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        x, y = self.__drawer.get_mouse_position(x - dx, y - dy)

        if self.__arena.is_in_bound(x, y):
            if self.__current_element == Element.WALL:
                self.__arena.add_elements(Wall(x, y))
            elif self.__current_element == Element.EMPTY_SPACE:
                self.__arena.add_elements((EmptySpace(x, y)))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == key.W:
            self.__current_element = Element.WALL
        elif symbol == key.E:
            self.__current_element = Element.EMPTY_SPACE
        elif symbol == key.N:
            self.__current_element = Element.END
        elif symbol == key.B:
            self.__current_element = Element.BEGINNING
        elif symbol == key.S:
            self.save_current_arena()
        elif symbol == key.P:
            path_finder = PersonalPathFinder(self.__arena)
            self.__path = path_finder.find_path(self.__beginning, self.__end, [])

    def save_current_arena(self):
        with open('./savedArena/test', 'wb') as file:
            pickle.dump(self.__arena, file)


def run():
    window = Gui()
    pyglet.app.run()
