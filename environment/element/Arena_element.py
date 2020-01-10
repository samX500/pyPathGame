class Arena_element():

    def __init__(self, x_pos: int, y_pos: int):
        self.__position = x_pos, y_pos

    def get_position(self):
        return self.__position
