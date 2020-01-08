from random import randint

from environment.Arena import Arena
from util.Direction import Direction

class Arena_factory():
    WALL_PROPORTION = 0.2

    @staticmethod
    def build_random_arena(width: int, height: int):
        arena = Arena(width, height)
        number_of_wall = width * height * Arena_factory.WALL_PROPORTION

        current_wall = 0

        while current_wall < number_of_wall:
            position = randint(width, height), randint(width, height)
            direction = Direction[randint(0, len(Direction))]
            min_size = min(width, height)
            lenght = randint(0, int(min_size / 4))

            walls = Arena_factory.build_wall(position, lenght, direction)
            arena.add_elements(walls)

            current_wall += len(walls)

        return arena

    @staticmethod
    def build_wall(position: (x, y), lenght, direction: Direction, size: (x, y)):
        walls = []

        for i in range(lenght):
            if 0 < position[x] < size[x] and 0 < position[y] < size[y]:
                walls.append(Wall(position.copy()))
                position += direction.get_value()
            else:
                break
        return walls
