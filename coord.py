class Coord:
    """Represents a coordinate on the board"""

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, obj):
        return isinstance(obj, Coord) and obj.i == self.i and obj.j == self.j

    def __str__(self):
        return f'{self.i}{self.j}'
