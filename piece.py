from colors import Colors
from coord import Coord


class Piece:
    """Represents a piece on the board"""
    color = Colors.BLUE
    name = ""
    coord = Coord(0, 0)

    def i(self):
        """Returns the i coordinate"""
        return self.coord.i

    def j(self):
        """Returns the j coordinate"""
        return self.coord.j

    def __init__(self, color, name, i, j):
        self.color = color
        self.name = name
        self.coord = Coord(i, j)
