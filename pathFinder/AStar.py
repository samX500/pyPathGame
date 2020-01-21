from environment.Arena import Arena
from environment.element.object.Wall import Wall
from pathFinder.PathFinder import PathFinder
from util.Direction import Direction


class AStar(PathFinder):

    def __init__(self, arena: Arena):
        super(AStar, self).__init__(arena)

    def find_path(self, begining: (int, int), end: (int, int)):
        start_node = Node(None, begining)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:
            print(len(open_list))
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []

                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]

            children = []

            for direction in Direction:

                node_position = current_node.position[0] + direction.value[0], current_node.position[1] + \
                                direction.value[1]

                if not self.arena.is_in_bound(*node_position):
                    continue

                if isinstance(self.arena.get_element_at(*node_position), Wall):
                    continue

                new_node = Node(current_node, node_position)

                children.append(new_node)

            for child in children:
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = (child.position[0] - end_node.position[0]) ** 2 + (
                        child.position[1] - end_node.position[1]) ** 2
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)


class Node:

    def __init__(self, parent, position: (int, int)):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)
