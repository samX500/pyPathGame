from environment.element.Arena_element import Arena_element


class Empty_space(Arena_element):

    def __init__(self, x_pos: int, y_pos: int):
        Arena_element.__init__(self, x_pos, y_pos)
