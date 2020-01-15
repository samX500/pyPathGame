class ElementColor():

    def __init__(self):
        self.__wall_color = None
        self.__empty_color = None
        self.__path_color = None
        self.__beginning_color = None
        self.__ending_color = None
        self.__element_char_color = None

    def get_wall_color(self):
        return self.__wall_color

    def set_wall_color(self, color: (int, int, int, int)):
        self.__wall_color = color

    def get_empty_color(self):
        return self.__empty_color

    def set_empty_color(self, color: (int, int, int, int)):
        self.__empty_color = color

    def get_element_char_color(self):
        return self.__element_char_color

    def set_element_char_color(self, color: (int, int, int, int)):
        self.__element_char_color = color

    def get_ending_color(self):
        return self.__ending_color

    def set_ending_color(self, color: (int, int, int, int)):
        self.__ending_color = color

    def get_beginning_color(self):
        return self.__beginning_color

    def set_beginning_color(self, color: (int, int, int, int)):
        self.__beginning_color = color

    def get_path_color(self):
        return self.__path_color

    def set_path_color(self, color: (int, int, int, int)):
        self.__path_color = color
