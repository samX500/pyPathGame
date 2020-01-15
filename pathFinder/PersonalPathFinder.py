import math

from environment import Arena
from pathFinder.PathFinder import PathFinder
from util.Direction import Direction


class PersonalPathFinder(PathFinder):

    def __init__(self, arena: Arena):
        PathFinder.__init__(self, arena)

    def find_path(self, begining: (int, int), end: (int, int), current_path: [(int, int)]):
        if begining == end:
            return current_path

        for direction in Direction:
            movement = begining[0] + direction.value[0], begining[1] + direction.value[1]
            if PersonalPathFinder.__is_closer(begining, movement, end):
                current_path.append(movement)
                return self.find_path(movement, end, current_path)

    @staticmethod
    def __is_closer(current_pos: (int, int), new_pos: (int, int), end_pos: (int, int)):
        return PersonalPathFinder.__get_distance(new_pos, end_pos) < PersonalPathFinder.__get_distance(current_pos,
                                                                                                       end_pos)

    @staticmethod
    def __get_distance(first_pos: (int, int), second_pos: (int, int)):
        return math.sqrt((second_pos[0] - first_pos[0]) ** 2 + (second_pos[1] - first_pos[1]) ** 2)
