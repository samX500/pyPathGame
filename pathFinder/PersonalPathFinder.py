import math

from environment import Arena
from environment.element.object.Wall import Wall
from pathFinder.PathFinder import PathFinder
from util.Direction import Direction


class PersonalPathFinder(PathFinder):

    def __init__(self, arena: Arena):
        super(PersonalPathFinder, self).__init__(arena)

    def find_path(self, beginning: (int, int), end: (int, int), current_path: [(int, int)], dead_end: [(int, int)]):
        print(current_path)

        if beginning == end:
            return current_path

        for direction in Direction:
            movement = beginning[0] + direction.value[0], beginning[1] + direction.value[1]
            if PersonalPathFinder.__is_closer(beginning, movement, end):
                if not isinstance(self.arena.get_element_at(*movement), Wall) and movement not in dead_end:
                    current_path.append(beginning)
                    return self.find_path(movement, end, current_path, dead_end)
                else:
                    for new_direction in Direction:
                        if new_direction != direction:
                            new_movement = beginning[0] + new_direction.value[0], beginning[1] + new_direction.value[1]
                            previous_step = current_path[-1]
                            if new_movement != previous_step and \
                                    not isinstance(self.arena.get_element_at(*new_movement), Wall) and \
                                    new_movement not in dead_end:

                                current_path.append(beginning)
                                return self.find_path(new_movement, end, current_path, dead_end)
                            else:
                                dead_end.append(beginning)
                                beginning = current_path.pop()
                                return self.find_path(beginning, end, current_path, dead_end)

    @staticmethod
    def __is_closer(current_pos: (int, int), new_pos: (int, int), end_pos: (int, int)):
        return PersonalPathFinder.__get_distance(new_pos, end_pos) < PersonalPathFinder.__get_distance(current_pos,
                                                                                                       end_pos)

    @staticmethod
    def __get_distance(first_pos: (int, int), second_pos: (int, int)):
        return math.sqrt((second_pos[0] - first_pos[0]) ** 2 + (second_pos[1] - first_pos[1]) ** 2)
