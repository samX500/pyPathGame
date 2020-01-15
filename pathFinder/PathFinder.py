import math

from environment.Arena import Arena
from util.Direction import Direction


class PathFinder():

    @staticmethod
    def find_path(arena: Arena, begining: (int, int), end: (int, int), current_path: [(int, int)]):
        if begining == end:
            return current_path

        for direction in Direction:
            movement = begining[0] + direction.value[0], begining[1] + direction.value[1]
            if PathFinder.__is_closer(begining, movement, end):
                current_path.append(movement)
                PathFinder.find_path(arena, movement, end, current_path)

        print('wtf')

    @staticmethod
    def __is_closer(current_pos: (int, int), new_pos: (int, int), end_pos: (int, int)):
        return PathFinder.__get_distance(new_pos, end_pos) < PathFinder.__get_distance(current_pos, new_pos)

    @staticmethod
    def __get_distance(first_pos: (int, int), second_pos: (int, int)):
        return math.sqrt((second_pos[0] - first_pos[0]) ** 2 + (second_pos[1] - first_pos[1])**2)
