from enum import Enum

class Direction(Enum):
    UP = [-1, 0]
    UP_RIGHT = [-1, 1]
    RIGHT = [0, 1]
    DOWN_RIGHT = [1, 1]
    DOWN = [1, 0]
    DOWN_LEFT = [1, -1]
    LEFT = [0, -1]
    UP_LEFT = [-1, -1]
    NONE = [0, 0]

    def get_value(self):
        return self.value.copy()

    def __str__(self):
        return self.name
