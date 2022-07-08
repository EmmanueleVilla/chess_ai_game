from coord import Coord


class Move:
    """Represents a move on the board"""
    start = Coord(0, 0)
    end = Coord(0, 0)

    def __init__(self, start, end):
        self.start = start
        self.end = end
