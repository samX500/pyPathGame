import pyglet.gl as gl

from environment.Arena import Arena
from environment.element import ArenaElement
from environment.element.object.EmptySpace import EmptySpace
from environment.element.object.Wall import Wall
from gui.ElementColor import ElementColor


class MazeDrawer():

    def __init__(self, colors: ElementColor, tile_size: int, board_dim: (int, int), window_dim: (int, int)):
        self.__colors = colors
        self.__tile_size = tile_size
        self.__board_width, self.__board_height = board_dim
        self.__window_width, self.__window_height = window_dim

        self.__transform = self.__window_width / 2 - self.__board_width / 2 * self.__tile_size, \
                           self.__window_width / 2 - self.__board_width / 2 * self.__tile_size, \
                           0

    def draw_arena(self, arena: Arena):
        gl.glPushMatrix()
        gl.glTranslatef(*self.__transform)

        dim = arena.get_dimension()

        for i in range(dim[0]):
            for j in range(dim[1]):
                gl.glPushMatrix()
                gl.glTranslatef(i * self.__tile_size, j * self.__tile_size, 0)

                element = arena.get_element_at(i, j)
                color = self.get_color(element)
                self.__draw_tile(color, self.__tile_size)

                gl.glPopMatrix()

        gl.glPopMatrix()

    def get_color(self, element: ArenaElement):

        if isinstance(element, Wall):
            return self.__colors.get_wall_color()
        elif isinstance(element, EmptySpace):
            return self.__colors.get_empty_color()

    def __draw_tile(self, color: (int, int, int, int), dimension: int):
        gl.glColor4f(*color)

        gl.glBegin(gl.GL_QUADS)
        gl.glVertex2d(0, 0)
        gl.glVertex2d(0, dimension)
        gl.glVertex2d(dimension, dimension)
        gl.glVertex2d(dimension, 0)
        gl.glEnd()
