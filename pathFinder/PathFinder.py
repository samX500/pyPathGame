from environment.Arena import Arena


class PathFinder():

    def __init__(self, arena: Arena):
        self.__arena = arena

    def find_path(self, begining: (int, int), end: (int, int), current_path: [(int, int)]):
        ...
