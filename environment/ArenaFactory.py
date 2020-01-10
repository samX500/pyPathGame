import random
from random import randint

from environment.Arena import Arena
from environment.element.object.Wall import Wall
from util.Direction import Direction


class ArenaFactory():
    WALL_PROPORTION = 0.2

    @staticmethod
    def build_random_arena(width: int, height: int):
        arena = Arena(width, height)
        number_of_wall = width * height * ArenaFactory.WALL_PROPORTION

        current_wall = 0

        while current_wall < number_of_wall:
            position = randint(0, width), randint(0, height)
            direction = random.choice(list(Direction))
            # TODO do a more proper length
            min_size = min(width, height)
            length = randint(1, int(min_size / 2))

            walls = ArenaFactory.build_wall(position, length, direction, arena)
            arena.add_elements(*walls)

            current_wall += len(walls)

        return arena

    @staticmethod
    def build_wall(position: (int, int), length, direction: Direction, arena:Arena):
        walls = []
        clone = position[0], position[1]
        for i in range(length):
            clone = clone[0], clone[1]
            if arena.is_in_bound(*clone):
                walls.append(Wall(*clone))
                clone = clone[0] + direction.get_value()[0], clone[1] + direction.get_value()[1]
            else:
                break
        return walls
