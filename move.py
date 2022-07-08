from coord import Coord


class Move:
    """Represents a move on the board"""

    def __init__(self, start, end):
        self.start = start
        self.end = end
