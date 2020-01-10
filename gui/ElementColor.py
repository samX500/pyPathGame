class ElementColor():

    def __init__(self):
        self.__wall_color = None
        self.__empty_color = None
        self.__player_color = None

    def get_wall_color(self):
        return self.__wall_color

    def set_wall_color(self, color: (int, int, int, int)):
        self.__wall_color = color

    def get_empty_color(self):
        return self.__empty_color

    def set_empty_color(self, color: (int, int, int, int)):
        self.__empty_color = color

    def get_player_color(self):
        return self.__player_color

    def set_player_color(self, color: (int, int, int, int)):
        self.__player_color = color
