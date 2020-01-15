from environment.element.ArenaElement import ArenaElement
from environment.element.object.EmptySpace import EmptySpace
from environment.element.object.Wall import Wall


class Arena():

    def __init__(self, width: int, height: int):
        self.__size = width, height
        self.__arena = self.__instantiate_area(*self.__size)

    @staticmethod
    def __instantiate_area(width: int, height: int):
        row = []
        for i in range(width):
            column = []
            for j in range(height):
                column.append(EmptySpace(i, j))
            row.append(column)
        return row

    def get_dimension(self):
        return self.__size

    def add_elements(self, *args: [ArenaElement]):
        for element in args:
            pos = element.get_position()
            if self.is_in_bound(*pos):
                self.__arena[pos[0]][pos[1]] = element
            else:
                raise Exception('position ', pos, ' is not within the boundaries of the playfield')

    def get_element_at(self, x: int, y: int):
        if self.is_in_bound(x, y):
            return self.__arena[x][y]
        else:
            raise Exception('position ', (x, y), ' is not within the boundaries of the playfield')

    def is_in_bound(self, x_pos: int, y_pos: int):
        return 0 <= x_pos < self.__size[0] and 0 <= y_pos < self.__size[1]


    def __str__(self):
        str = ''

        for column in self.__arena:
            for element in column:
                if isinstance(element, EmptySpace):
                    str += 'E '
                elif isinstance(element, Wall):
                    str += 'W '
            str += '\n'

        return str
