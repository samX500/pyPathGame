from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def get_value(self):
        return self.value

    def __str__(self):
        return self.name
