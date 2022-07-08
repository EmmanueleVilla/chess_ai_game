from colors import colors
from coord import Coord


class Piece:
    color = colors.BLUE
    type = ""
    coord = Coord(0, 0)

    def i(self):
        return self.coord.i
    
    def j(self):
        return self.coord.j

    def __init__(self, color, type, coord):
        self.color = color
        self.type = type
        self.coord = coord

    def __init__(self, color, type, i, j):
        self.color = color
        self.type = type
        self.coord = Coord(i, j)