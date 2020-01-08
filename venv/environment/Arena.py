from environment.Arena_factory import Arena_factory
from environment.element.object.Empty_space import Empty_space
from environment.element.object.Wall import Wall

class Arena():

    def __init__(self,size:(x,y)):
        self.__size = size
        self.__arena = self.__instantiate_area(self.__size)

    @staticmethod
    def __instantiate_area(size:(x,y)):
        row = []
        for i in range(x):
            for j in range(y):
                column = []
                column.append(Empty_space(i,j))
                row.append(column)
        return row

    def add_element(self,element:Arena_element):
        pos = element.get_position()
        self.__arena[pos[0]][pos[1]] = element

    def add_elements(self,elements:list(ArenaElement)):
        for element in elements:
            pos = element.get_position()
            self.__arena[pos[0]][pos[1]] = element

    def __str__(self):
        str = ''

        for column in self.__arena:
            for element in column:
                if isinstance(element, Empty_space):
                    str += 'E '
                elif isinstance(element, Wall):
                    str += 'W '
            str += '\n'

        return str

    if __name__ == '__main__':
        arena = Arena_factory.build_random_arena(20,20)
        print(arena)