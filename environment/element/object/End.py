from environment.element.ArenaElement import ArenaElement


class End(ArenaElement):

    def __init__(self, x_pos: int, y_pos: int):
        ArenaElement.__init__(self, x_pos, y_pos)
