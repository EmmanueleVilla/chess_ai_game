from coord import Coord


class Piece:
    """Represents a piece on the board"""

    def i(self):
        """Returns the i coordinate"""
        return self.coord.i

    def i_as_letter(self):
        """Returns the i coordinate as a letter"""
        assert self.coord.i > 0
        letters = "a b c d e f g h".split(" ")
        return letters[self.coord.i - 1]

    def j(self):
        """Returns the j coordinate"""
        return self.coord.j

    def __init__(self, color, name, i, j, moved=False):
        self.color = color
        self.name = name
        self.coord = Coord(i, j)
        self.moved = moved

    def __eq__(self, obj):
        return (
                isinstance(obj, Piece)
                and obj.coord == self.coord
                and obj.color == self.color
                and obj.name == self.name
        )

    def __str__(self):
        return f'{self.name}{self.color}: {self.i_as_letter()}{self.j()}'
